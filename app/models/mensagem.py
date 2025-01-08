from app import db
from datetime import date

class Mensagem(db.Model):
    __tablename__ = 'mensagens'

    id_mensagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    data_envio = db.Column(db.Date, nullable=False, default=date.today)
    conteudo = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(50))  # Ex.: "Cobrança", "Progresso", etc.
