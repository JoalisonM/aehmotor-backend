from flask_restful import fields
from helpers.database import db
from model.funcionario import Funcionario


motorista_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'cargo' : fields.String,
  'senha' : fields.String,
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
    return f'< Rota{self.id} Veiculo {self.id}>'


