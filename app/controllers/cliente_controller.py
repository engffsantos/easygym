from flask import Blueprint, request, jsonify
from extensions import db
from app.models.cliente import Cliente

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{
        'id_cliente': cliente.id_cliente,
        'nome': cliente.nome,
        'whatsapp': cliente.whatsapp,
        'status_pagamento': cliente.status_pagamento
    } for cliente in clientes])
