from flask import Flask
from config import Config
from extensions import db, migrate
from app.controllers import (
    cliente_bp,
    exercicio_bp,
    treino_bp,
    pagamento_bp,
    medida_bp
)
from app.views import (
    cliente_views_bp,
    exercicio_views_bp,
    treino_views_bp,
    pagamento_views_bp
)

def create_app():
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa as extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra as blueprints dos controladores (API)
    app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
    app.register_blueprint(exercicio_bp, url_prefix='/api/exercicios')
    app.register_blueprint(treino_bp, url_prefix='/api/treinos')
    app.register_blueprint(pagamento_bp, url_prefix='/api/pagamentos')
    app.register_blueprint(medida_bp, url_prefix='/api/medidas')

    # Registra as blueprints das views (templates)
    app.register_blueprint(cliente_views_bp, url_prefix='/clientes')
    app.register_blueprint(exercicio_views_bp, url_prefix='/exercicios')
    app.register_blueprint(treino_views_bp, url_prefix='/treinos')
    app.register_blueprint(pagamento_views_bp, url_prefix='/pagamentos')

    return app
