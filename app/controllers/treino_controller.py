from flask import Blueprint, request, jsonify
from app.models.treino import Treino, TreinoExercicios
from app import db

treino_bp = Blueprint('treino_bp', __name__)

@treino_bp.route('/treinos', methods=['GET'])
def listar_treinos():
    treinos = Treino.query.all()
    return jsonify([{
        'id_treino': treino.id_treino,
        'nome': treino.nome,
        'descricao': treino.descricao
    } for treino in treinos])

@treino_bp.route('/treinos', methods=['POST'])
def criar_treino():
    dados = request.json
    novo_treino = Treino(
        nome=dados['nome'],
        descricao=dados.get('descricao')
    )
    db.session.add(novo_treino)
    db.session.commit()
    return jsonify({'mensagem': 'Treino criado com sucesso!'}), 201
