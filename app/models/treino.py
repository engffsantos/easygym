from app import db

class Treino(db.Model):
    __tablename__ = 'treinos'

    id_treino = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

    exercicios = db.relationship('TreinoExercicios', backref='treino', lazy=True)
    clientes = db.relationship('ClienteTreinos', backref='treino', lazy=True)

class TreinoExercicios(db.Model):
    __tablename__ = 'treino_exercicios'

    id_treino = db.Column(db.Integer, db.ForeignKey('treinos.id_treino'), primary_key=True)
    id_exercicio = db.Column(db.Integer, db.ForeignKey('exercicios.id_exercicio'), primary_key=True)
    series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)

class ClienteTreinos(db.Model):
    __tablename__ = 'cliente_treinos'

    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), primary_key=True)
    id_treino = db.Column(db.Integer, db.ForeignKey('treinos.id_treino'), primary_key=True)
    peso_exercicio = db.Column(db.Numeric(5, 2))
    data_inicio = db.Column(db.Date)
    data_fim = db.Column(db.Date)
