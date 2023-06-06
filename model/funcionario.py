from flask_restful import fields
from helpers.database import db
from model.pessoa import Pessoa

funcionario_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.String,
  'email': fields.String,
  'telefone': fields.String,
  'senha' : fields.String,
  'cargo' : fields.String,
}

class Funcionario(Pessoa):
  
  __tablename__ = "funcionario"

  idPessoa = db.Column(db.Integer ,db.ForeignKey("pessoa.id"), primary_key=True)
  cargo = db.Column(db.String, nullable=False)

  prefeitura = db.relationship("Prefeitura", uselist=False, backref="funcionario")

  __mapper_args__ = {
    "polymorphic_identity": "funcionario"
  }

  def __init__(self, nome, email, nascimento, telefone, senha, cargo):
    super().__init__(nome, email, nascimento, telefone, senha)
    self.cargo = cargo

  def __repr__(self):
    return f'<Funcionario>'