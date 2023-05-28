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
  __tablename__ = "endereco"

  id = db.Column(db.Integer, primary_key=True)
  idPessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
  cep = db.Column(db.String, nullable=False)
  numero = db.Column(db.Integer, nullable=False)
  complemento = db.Column(db.String, nullable=False)
  referencia = db.Column(db.String, nullable=False)
  logradouro = db.Column(db.String, nullable=False)
  idCidade = db.Column(db.Integer, db.ForeignKey('cidade.id'))

  prefeitura = db.relationship("Prefeitura", uselist=False, backref="endereco")
  instituicaoEnsino = db.relationship("InstituicaoEnsino", uselist=False, backref="endereco")

  def __init__(self, cep, numero, complemento, referencia, logradouro, idCidade, idPessoa):
    self.cep = cep
    self.numero = numero
    self.idCidade = idCidade
    self.referencia = referencia
    self.logradouro = logradouro
    self.complemento = complemento

  def __repr__(self):
    return f'<Endereço>'
