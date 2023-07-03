from flask_restful import fields
import datetime
from helpers.database import db
from model.viagem import viagem_fields
from model.aluno import aluno_fields

pretensao_fields = {
    'id': fields.Integer,
    'viagem': fields.Nested(viagem_fields),
    'aluno': fields.Nested(aluno_fields),
    'embarque': fields.Boolean,
    'data_embarque': fields.String,
    'criacao':fields.String


class Pretensao(db.Model):
    __tablename__ = "pretensao"

    id = db.Column(db.Integer, primary_key=True)
    id_viagem = db.Column(db.Integer, db.ForeignKey('viagem.id'))
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id_pessoa'))

    embarque = db.Column(db.Boolean, nullable=False)
    data_embarque = db.Column(db.DateTime, nullable=False)

    criacao = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.utcnow)

    def __init__(self, id_viagem, id_aluno, embarque, data_embarque):
        self.id_viagem = id_viagem
        self.id_aluno = id_aluno
        self.embarque = embarque
        self.data_embarque = data_embarque

    def __repr__(self):
        return f'<Pretensao viagem={self.viagem}, aluno={self.aluno}>'