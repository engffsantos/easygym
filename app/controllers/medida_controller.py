from flask import Blueprint, request, jsonify
from app.models.medida import Medida
from app import db

medida_bp = Blueprint('medida_bp', __name__)

@medida_bp.route('/medidas', methods=['GET'])
def listar_medidas():
    medidas = Medida.query.all()
    return jsonify([{
        'id_medida': medida.id_medida,
        'id_cliente': medida.id_cliente,
        'data_medicao': medida.data_medicao,
        'peso': medida.peso,
        'altura': medida.altura
    } for medida in medidas])

@medida_bp.route('/medidas', methods=['POST'])
def registrar_medida():
    dados = request.json
    nova_medida = Medida(
        id_cliente=dados['id_cliente'],
        data_medicao=dados['data_medicao'],
        peso=dados.get('peso'),
        altura=dados.get('altura'),
        braco=dados.get('braco'),
        perna=dados.get('perna'),
        cintura=dados.get('cintura'),
        observacoes=dados.get('observacoes')
    )
    db.session.add(nova_medida)
    db.session.commit()
    return jsonify({'mensagem': 'Medida registrada com sucesso!'}), 201
