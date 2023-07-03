from flask_restful import fields
from helpers.database import db
from model.rota import rota_fields
from model.veiculo import veiculo_fields
from model.motorista import motorista_fields
import datetime

viagem_fields = {
    'id': fields.Integer,
    'rota': fields.Nested(rota_fields),
    'veiculo': fields.Nested(veiculo_fields),
    'motorista': fields.Nested(motorista_fields),
    'data_viagem': fields.String,
    'criacao':fields.String
}

class Viagem(db.Model):
    __tablename__ = "viagem"

    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey('rota.id'))
    id_funcionario = db.Column(db.Integer, db.ForeignKey('motorista.id_funcionario'))
    id_veiculo = db.Column(db.Integer,db.ForeignKey('veiculo.id'))
    data_viagem = db.Column(db.DateTime, nullable=False)
    criacao = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)

    pretensao = db.relationship("Pretensao", uselist=False, backref="viagem")


    def __init__(self, id_rota,id_funcionario,id_veiculo, data_viagem):
        self.id_rota = id_rota
        self.id_funcionario = id_funcionario
        self.id_veiculo = id_veiculo
        self.data_viagem = data_viagem

    def __repr__(self):
        return f'<Data da viagem = {self.data}>'