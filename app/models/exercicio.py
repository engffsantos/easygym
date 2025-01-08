from app import db

class Exercicio(db.Model):
    __tablename__ = 'exercicios'

    id_exercicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    grupo_muscular = db.Column(db.String(50))
    descricao = db.Column(db.Text)

    treinos = db.relationship('TreinoExercicios', backref='exercicio', lazy=True)
