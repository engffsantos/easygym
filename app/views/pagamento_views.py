from flask import Blueprint, render_template
from app.models.pagamento import Pagamento

pagamento_views_bp = Blueprint('pagamento_views', __name__, template_folder='templates')

@pagamento_views_bp.route('/pagamentos')
def listar_pagamentos():
    pagamentos = Pagamento.query.all()
    return render_template('pagamentos/lista.html', pagamentos=pagamentos)
