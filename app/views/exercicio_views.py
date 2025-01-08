from flask import Blueprint, render_template
from app.models.exercicio import Exercicio

exercicio_views_bp = Blueprint('exercicio_views', __name__, template_folder='templates')

@exercicio_views_bp.route('/exercicios')
def listar_exercicios():
    exercicios = Exercicio.query.all()
    return render_template('exercicios/lista.html', exercicios=exercicios)
