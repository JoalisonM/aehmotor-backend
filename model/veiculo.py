from flask_restful import fields
from helpers.database import db


veiculo_fields={
  'id':fields.Integer,
  'cidade':fields.String,
  'qtd_passageiros':fields.Integer,
  'tipo_veiculo':fields.String,
  'placa':fields.String,
}

class Veiculo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cidade = db.Column(db.String, nullable=False)
  qtd_passageiros = db.Column(db.Integer, nullable=False)
  tipo_veiculo = db.Column(db.String, nullable=False)
  placa = db.Column(db.String, nullable=False)

  rota = db.relationship("Rota", uselist=False, backref="veiculo")
  viagem = db.relationship("Viagem", uselist=False, backref="veiculo")
  motorista = db.relationship("Motorista", uselist=False, backref="veiculo")

  def __init__(self, cidade, qtd_passageiros, tipo_veiculo, placa):
    self.cidade=cidade
    self.qtd_passageiros=qtd_passageiros
    self.tipo_veiculo=tipo_veiculo
    self.placa=placa

  def __repr__(self):
    return f'<Veiculo {self.id}>'