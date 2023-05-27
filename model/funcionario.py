from flask_restful import fields
from helpers.database import db
from model.pessoa import *
#from model.prefeitura import prefeitura_fields

funcionario_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'endereco': endereco_fields,
  #'prefeitura': prefeitura_fields,
  'cargo' : fields.String,
}

class Funcionario(Pessoa, db.Model):

  __mapper_args__ = {'polymorphic_identify': 'funcionario'}

  #id = db.relationship("Pessoa", useList=False, backref="pessoa")
  #prefeitura = db.relationship("Prefeitura", useList=False, backref="funcionario")
  cargo = db.Column(db.String, unique=True, nullable=False)

  def __init__(self, nome, nascimento, email, telefone, idEndereco, prefeitura, cargo):
    super().__init__(nome, nascimento, email, telefone, idEndereco)
    self.prefeitura = prefeitura
    self.cargo = cargo
    
  def __repr__(self):
    return f'<Funcionario>'