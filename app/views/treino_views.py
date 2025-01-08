from flask import Blueprint, render_template
from app.models.treino import Treino

treino_views_bp = Blueprint('treino_views', __name__, template_folder='templates')

@treino_views_bp.route('/treinos')
def listar_treinos():
    treinos = Treino.query.all()
    return render_template('treinos/lista.html', treinos=treinos)

@treino_views_bp.route('/treinos/<int:id_treino>')
def detalhes_treino(id_treino):
    treino = Treino.query.get_or_404(id_treino)
    return render_template('treinos/detalhes.html', treino=treino)
