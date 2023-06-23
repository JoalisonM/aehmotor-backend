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
parser.add_argument('secretario', type=str, help='Problema no id do secretario', required=True)
parser.add_argument('id_endereco', type=str, help='Problema no telefone', required=True)
parser.add_argument('nome', type=str, help='Problema no nome', required=True)


class Prefeituras(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Prefeituras listados com sucesso!")
        prefeituras = Prefeitura.query.all()
        return marshal(prefeituras, prefeitura_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            secretario = args["secretario"]
            id_endereco = args["id_endereco"]

            prefeitura = Prefeitura(secretario, id_endereco)

            db.session.add(prefeitura)
            db.session.commit()

            logger.info("Prefeitura cadastrada com sucesso!")

            return marshal(prefeitura, prefeitura_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Uf", 2)
            return marshal(message, message_fields), 404

class PrefeituraById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        prefeitura = Prefeitura.query.get(id)

        if prefeitura is None:
            logger.error(f"Prefeitura {id} não encontrado")

            message = Message(f"Prefeitura {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Prefeitura {id} encontrado com sucesso!")
        return marshal(prefeitura, prefeitura_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            prefeitura = Prefeitura.query.get(id)

            if prefeitura is None:
                logger.error(f"Prefeitura {id} não encontrado")
                message = Message(f"Prefeitura {id} não encontrado", 1)
                return marshal(message, message_fields)

            prefeitura.nome = args["nome"]
            prefeitura.secretario = args["secretario"]
            prefeitura.id_endereco = args["id_endereco"]

            db.session.add(prefeitura)
            db.session.commit()

            logger.info("Prefeitura cadastrado com sucesso!")
            return marshal(prefeitura, prefeitura_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Uf", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token,token_tipo, id):
        prefeitura = Prefeitura.query.get(id)

        if prefeitura is None:
            logger.error(f"Prefeitura {id} não encontrado")
            message = Message(f"Prefeitura {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(prefeitura)
        db.session.commit()

        message = Message("Prefeitura deletado com sucesso!", 3)
        return marshal(message, message_fields), 200