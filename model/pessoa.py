from flask import Flask
from flask_restful import fields
from helpers.database import db
from model.endereco import endereco_fields

pessoa_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'endereco': endereco_fields,
  'senha':fields.String,
}

class Pessoa(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  nascimento = db.Column(db.Date, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  telefone = db.Column(db.String, unique=True, nullable=False)
  idEndereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))

  def __init__(self, nome, email, nascimento, telefone, idEndereco):
    self.nome = nome
    self.email = email
    self.nascimento = nascimento
    self.telefone = telefone
    self.idEndereco = idEndereco

  def __repr__(self):
    return f'<Pessoa {self.nome}>'