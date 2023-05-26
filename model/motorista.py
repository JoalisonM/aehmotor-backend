from flask_restful import fields
from helpers.database import db
from model.rota import Rota,rota_fields
from model.veiculo import Veiculo,veiculo_fields


motorista_fields = {

    'rota': fields.Nested(rota_fields),
    'veiculo': fields.Nested(veiculo_fields)
}

class Motorista(db.Model):
    
    rota_id = db.Column(db.Integer, db.ForeignKey("rota.id"))
    rota = db.relationship("Rota", uselist=False)

    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculo.id"))
    veiculo = db.relationship("Veiculo", uselist=False)
    
def __init__(self,rota: Rota,veiculo:Veiculo):
     self.rota = rota
     self.veiculo=veiculo
     
def __repr__(self):
    return f'< Rota{self.id} Veiculo {self.id}>'


