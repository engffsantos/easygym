from app import db
from datetime import date

class Medida(db.Model):
    __tablename__ = 'medidas'

    id_medida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    data_medicao = db.Column(db.Date, nullable=False, default=date.today)
    peso = db.Column(db.Numeric(5, 2))
    altura = db.Column(db.Numeric(5, 2))
    braco = db.Column(db.Numeric(5, 2))
    perna = db.Column(db.Numeric(5, 2))
    cintura = db.Column(db.Numeric(5, 2))
    observacoes = db.Column(db.Text)
    progresso_foto = db.Column(db.LargeBinary)
