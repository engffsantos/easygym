from app import db
from datetime import date

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'

    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    data_pagamento = db.Column(db.Date, nullable=False, default=date.today)
    data_vencimento = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    forma_pagamento = db.Column(db.String(50))
    comprovante = db.Column(db.LargeBinary)
    observacoes = db.Column(db.Text)
