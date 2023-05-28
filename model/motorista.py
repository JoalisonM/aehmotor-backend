from flask_restful import fields
from helpers.database import db
from model.funcionario import Funcionario


motorista_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'idEndereco': fields.Integer,
  'cargo' : fields.String,
  'senha' : fields.String,
  'idVeiculo' : fields.Integer,
}

class Motorista(Funcionario):
  __tablename__ = "motorista"

  idFuncionario = db.Column(db.Integer ,db.ForeignKey("funcionario.idPessoa"), primary_key=True)
  idVeiculo = db.Column(db.Integer, db.ForeignKey("veiculo.id"))

  rota = db.relationship("Rota", uselist=False, backref="motorista")

  __mapper_args__ = {"polymorphic_identity": "motorista"}

  def __init__(self, nome, nascimento, email, telefone, senha, idEndereco, cargo, idVeiculo):
    super().__init__(nome, nascimento, email, telefone, senha, idEndereco, cargo)
    self.idVeiculo = idVeiculo

  def __repr__(self):
    return f'< Rota{self.id} Veiculo {self.id}>'


