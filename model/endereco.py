from flask_restful import fields
from helpers.database import db

endereco_fields = {
  'id': fields.Integer,
  'cep': fields.String,
  'numero': fields.String,
  'complemento': fields.String,
  'referencia': fields.String,
  'logradouro': fields.String,
}

class Endereco(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cep = db.Column(db.String, nullable=False)
  numero = db.Column(db.String, nullable=False)
  complemento = db.Column(db.String, nullable=False)
  referencia = db.Column(db.String, nullable=False)
  logradouro = db.Column(db.String, nullable=False)
  pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))

  def __init__(self):
    pass

  def __repr__(self):
    return f'<Endereço>'
