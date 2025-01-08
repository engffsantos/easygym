from flask import Blueprint, request, jsonify
from app.models.exercicio import Exercicio
from app import db

exercicio_bp = Blueprint('exercicio_bp', __name__)

@exercicio_bp.route('/exercicios', methods=['GET'])
def listar_exercicios():
    exercicios = Exercicio.query.all()
    return jsonify([{
        'id_exercicio': exercicio.id_exercicio,
        'nome': exercicio.nome,
        'grupo_muscular': exercicio.grupo_muscular
    } for exercicio in exercicios])

@exercicio_bp.route('/exercicios', methods=['POST'])
def criar_exercicio():
    dados = request.json
    novo_exercicio = Exercicio(
        nome=dados['nome'],
        grupo_muscular=dados.get('grupo_muscular'),
        descricao=dados.get('descricao')
    )
    db.session.add(novo_exercicio)
    db.session.commit()
    return jsonify({'mensagem': 'Exercício criado com sucesso!'}), 201
