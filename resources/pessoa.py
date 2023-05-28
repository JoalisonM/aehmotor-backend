import datetime
from flask_restful import Resource, reqparse, marshal_with, marshal

from model.aluno import *
from model.cidade import *
from model.endereco import *
from model.funcionario import *
from model.instituicaoEnsino import *
from model.message import *
from model.motorista import *
from model.passageiro import *
from model.pessoa import *
from model.prefeitura import *
from model.rota import *
from model.uf import *
from helpers.database import db
# from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Problema no nome', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('nascimento', type=datetime,
                    help='Problema no nascimento', required=True)
parser.add_argument('telefone', type=str,
                    help='Problema no telefone', required=True)
parser.add_argument('senha', type=str,
                    help='Problema na senha', required=True)
parser.add_argument('idEndereco', type=int,
                    help='Problema no endereço', required=True)


class PessoaResource(Resource):
    @marshal_with(pessoa_fields)
    def get(self):
        pessoas = Pessoa.query.all()
        return pessoas, 200

    @marshal_with(pessoa_fields)
    def post(self):
        args = parser.parse_args()
        name = args["name"]
        email = args["email"]
        nascimento = args["nascimento"]
        telefone = args["telefone"]
        idEndereco = args["idEndereco"]
        senha = args["senha"]

        pessoa = Pessoa(name, email, nascimento, telefone, senha, idEndereco)

        db.session.add(pessoa)
        db.session.commit()

        return pessoa, 201
