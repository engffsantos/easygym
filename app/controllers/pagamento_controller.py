from flask import Blueprint, request, jsonify
from app.models.pagamento import Pagamento
from app import db

pagamento_bp = Blueprint('pagamento_bp', __name__)

@pagamento_bp.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    pagamentos = Pagamento.query.all()
    return jsonify([{
        'id_pagamento': pagamento.id_pagamento,
        'id_cliente': pagamento.id_cliente,
        'data_pagamento': pagamento.data_pagamento,
        'valor': pagamento.valor,
        'status': pagamento.status
    } for pagamento in pagamentos])

@pagamento_bp.route('/pagamentos', methods=['POST'])
def registrar_pagamento():
    dados = request.json
    novo_pagamento = Pagamento(
        id_cliente=dados['id_cliente'],
        data_pagamento=dados['data_pagamento'],
        data_vencimento=dados['data_vencimento'],
        valor=dados['valor'],
        status=dados['status']
    )
    db.session.add(novo_pagamento)
    db.session.commit()
    return jsonify({'mensagem': 'Pagamento registrado com sucesso!'}), 201
