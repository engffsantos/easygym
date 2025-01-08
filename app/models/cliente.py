from extensions import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(20), nullable=False)
    data_cadastro = db.Column(db.Date, nullable=False)
    status_pagamento = db.Column(db.Boolean, default=False)
    ultima_mensalidade = db.Column(db.Date)
    observacoes = db.Column(db.Text)
    plano = db.Column(db.String(50))
    dia_vencimento = db.Column(db.Integer)
    ativo = db.Column(db.Boolean, default=True)  # Campo para indicar se o cliente está ativo


    medidas = db.relationship('Medida', backref='cliente', lazy=True)
    pagamentos = db.relationship('Pagamento', backref='cliente', lazy=True)
    treinos = db.relationship('ClienteTreinos', backref='cliente', lazy=True)
