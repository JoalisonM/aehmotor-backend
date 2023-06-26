from flask_restful import fields
import datetime
from helpers.database import db
from model.viagem import viagem_fields
from model.aluno import aluno_fields

pretencao_fields = {
    'id': fields.Integer,
    'viagem': fields.Nested(viagem_fields),
    'aluno': fields.Nested(aluno_fields),
}


class Pretencao(db.Model):
    __tablename__ = "pretencao"

    # SQL
    id = db.Column(db.Integer, primary_key=True)
    id_viagem = db.Column(db.Integer, db.ForeignKey('viagem.id'))
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id_pessoa'))

    embarque = db.Column(db.Boolean, nullable=False)
    data_embarque = db.Column(db.DateTime, nullable=False)

    criacao = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.utcnow)

    # OO
    viagem = db.relationship("Viagem", uselist=False)
    aluno = db.relationship("Aluno", uselist=False)

    def __init__(self, viagem, aluno, embarque, data_embarque):
        self.viagem = viagem
        self.aluno = aluno
        self.embarque = embarque
        self.data_embarque = data_embarque

    def __repr__(self):
        return f'<Pretencao viagem={self.viagem}, aluno={self.aluno}>'
