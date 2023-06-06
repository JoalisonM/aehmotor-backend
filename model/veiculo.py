from flask_restful import fields
from helpers.database import db

veiculo_fields={
  'id':fields.Integer,
  'cidade':fields.String,
  'qtdPassageiros':fields.Integer,
  'tipoVeiculo':fields.String,
  'placa':fields.String,
}

class Veiculo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cidade = db.Column(db.String, nullable=False)
  qtd_passageiros = db.Column(db.Integer, nullable=False)
  tipo_veiculo = db.Column(db.String, nullable=False)
  placa = db.Column(db.String, nullable=False)

  rota = db.relationship("Rota", uselist=False, backref="veiculo")
  motorista = db.relationship("Motorista", uselist=False, backref="veiculo")

  def __init__(self, cidade, qtdPassageiros, tipoVeiculo, placa):
    self.cidade=cidade
    self.qtdPassageiros=qtdPassageiros
    self.tipoVeiculo=tipoVeiculo
    self.placa=placa

  def __repr__(self):
    return f'<Veiculo {self.id}>'