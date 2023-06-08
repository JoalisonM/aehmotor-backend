from flask_restful import fields
from helpers.database import db

endereco_fields = {
  'id': fields.Integer,
  'id_pessoa': fields.Integer,
  'id_cidade': fields.Integer,
  'cep': fields.String,
  'numero': fields.Integer,
  'complemento': fields.String,
  'referencia': fields.String,
  'logradouro': fields.String,
}

class Endereco(db.Model):
  __tablename__ = "endereco"

  id = db.Column(db.Integer, primary_key=True)
  id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
  id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.codigo_ibge'), nullable=False)
  cep = db.Column(db.String, nullable=False)
  numero = db.Column(db.Integer, nullable=False)
  complemento = db.Column(db.String, nullable=False)
  referencia = db.Column(db.String, nullable=False)
  logradouro = db.Column(db.String, nullable=False)

  prefeitura = db.relationship("Prefeitura", uselist=False, backref="endereco")
  instituicao_ensino = db.relationship("InstituicaoEnsino", uselist=False, backref="endereco")

  def __init__(self, cep, numero, complemento, referencia, logradouro, id_cidade, id_pessoa):
    self.cep = cep
    self.numero = numero
    self.id_cidade = id_cidade
    self.id_pessoa = id_pessoa
    self.referencia = referencia
    self.logradouro = logradouro
    self.complemento = complemento

  def __repr__(self):
    return f'<Endereço>'
