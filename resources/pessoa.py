import datetime
from flask_restful import Resource, reqparse, marshal_with, marshal

from model.pessoa import *
from model.endereco import *
from model.cidade import *
from model.institutoEnsino import *
from model.uf import *
from model.message import *
from helpers.database import db
# from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Problema no nome', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('nascimento', type=datetime,
                    help='Problema no nascimento', required=True)
parser.add_argument('telefone', type=str,
                    help='Problema no telefone', required=True)
parser.add_argument('endereco', type=dict,
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
        endereco = args["endereco"]

        pessoa = Pessoa(name, email, nascimento, telefone, endereco)

        db.session.add(pessoa)
        db.session.commit()

        return pessoa, 201
