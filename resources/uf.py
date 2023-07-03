from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.aluno import *
from model.instituicaoEnsino import *
from model.endereco import *
from model.cidade import *
from model.uf import *
from model.prefeitura import *
from model.funcionario import *
from model.passageiro import *
from model.motorista import *
from model.pessoa import *
from model.veiculo import *
from model.rota import *
from model.message import *
from helpers.database import db
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('sigla', type=str, help='Problema no sigla', required=True)
"""parser.add_argument('latitude', type=float, help='Problema no latitude', required=True)
parser.add_argument('longitude', type=float, help='Problema no longitude', required=True)
parser.add_argument('regiao', type=str, help='Problema no região', required=True)"""


class Ufs(Resource):
    def get(self):
        logger.info("Ufs listadas com sucesso!")
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Ufs listados com sucesso!")
        ufs = Uf.query.all()
        return marshal(ufs, uf_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            sigla = args["sigla"]
            #latitude = args["latitude"]
            #longitude = args["longitude"]
            #regiao = args["regiao"]

            uf = Uf(nome, sigla)

            db.session.add(uf)
            db.session.commit()

            logger.info("Uf cadastrado com sucesso!")

            return marshal(uf, uf_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Uf", 2)
            return marshal(message, message_fields), 404

class UfById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo,id):
        uf = Uf.query.get(id)

        if uf is None:
            logger.error(f"Uf {id} não encontrado")

            message = Message(f"Uf {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Instituição de Ensino {id} encontrado com sucesso!")
        return marshal(uf, uf_fields)

    @token_verifica
    def put(self, refresh_token,token_tipo,id):
        args = parser.parse_args()

        try:
            uf = Uf.query.get(id)

            if uf is None:
                logger.error(f"Uf {id} não encontrado")
                message = Message(f"Uf {id} não encontrado", 1)
                return marshal(message, message_fields)

            uf.nome = args["nome"]
            uf.sigla = args["sigla"]

            db.session.add(uf)
            db.session.commit()

            logger.info("Uf cadastrado com sucesso!")
            return marshal(uf, uf_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Uf", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, id):
        uf = Uf.query.get(id)

        if uf is None:
            logger.error(f"Uf {id} não encontrado")
            message = Message(f"Uf {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(uf)
        db.session.commit()

        message = Message("Uf deletado com sucesso!", 3)
        return marshal(message, message_fields), 200

class UfByNome(Resource):
    def get(self, nome):
        uf = Uf.query.filter_by(nome=nome).all()

        if uf is None:
            logger.error(f"Uf {id} não encontrado")

            message = Message(f"Uf {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Uf {id} encontrado com sucesso!")
        return marshal(uf, uf_fields), 200