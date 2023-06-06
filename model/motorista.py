from flask_restful import fields
from helpers.database import db
from model.funcionario import Funcionario
from model.endereco import Endereco



motorista_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.String,
  'email': fields.String,
  'telefone': fields.String,
  'senha' : fields.String,
  'cargo':fields.String,
  'idVeiculo' : fields.Integer,
}

class Motorista(Funcionario):
  __tablename__ = "motorista"

  id_funcionario = db.Column(db.Integer ,db.ForeignKey("funcionario.id_pessoa"), primary_key=True)
  id_veiculo = db.Column(db.Integer, db.ForeignKey("veiculo.id"))

  __mapper_args__ = {"polymorphic_identity": "motorista"}

  def __init__(self, nome, nascimento, email, telefone, senha, cargo, idVeiculo):
    super().__init__(nome, nascimento, email, telefone, senha, cargo)
    self.idVeiculo = idVeiculo

  def __repr__(self):
    return f'< Veiculo {self.id}>'


