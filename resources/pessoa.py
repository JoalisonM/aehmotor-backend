from flask_restful import Resource, reqparse, marshal

from model.pessoa import *
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('nascimento', type=str, help='Problema no nascimento', required=True)
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('senha', type=str, help='Problema na senha', required=True)


class Pessoas(Resource):
    def get(self):
        logger.info("Pessoas listadas com sucesso!")
        pessoas = Pessoa.query.all()
        return marshal(pessoas, pessoa_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            email = args["email"]
            nascimento = args["nascimento"]
            telefone = args["telefone"]
            senha = args["senha"]

            pessoa = Pessoa(nome, email, nascimento, telefone, senha)

            db.session.add(pessoa)
            db.session.commit()

            logger.info("Pessoa cadastrada com sucesso!")

            return marshal(pessoa, pessoa_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar pessoa", 2)
            return marshal(message, message_fields), 404

class PessoaById(Resource):
    def get(self, id):
        pessoa = Pessoa.query.get(id)

        if pessoa is None:
            logger.error(f"Pessoa {id} não encontrada")

            message = Message(f"Pessoa {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Pessoa {id} encontrada com sucesso!")
        return marshal(pessoa, pessoa_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            pessoa = Pessoa.query.get(id)

            if pessoa is None:
                logger.error(f"Pessoa {id} não encontrada")
                message = Message(f"Pessoa {id} não encontrada", 1)
                return marshal(message, message_fields)

            pessoa.nome = args["nome"]
            pessoa.email = args["email"]
            pessoa.nascimento = args["nascimento"]
            pessoa.telefone = args["telefone"]
            pessoa.senha = args["senha"]

            db.session.add(pessoa)
            db.session.commit()

            logger.info("Pessoa cadastrada com sucesso!")
            return marshal(pessoa, pessoa_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar pessoa", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        pessoa = Pessoa.query.get(id)

        if pessoa is None:
            logger.error(f"Pessoa {id} não encontrada")
            message = Message(f"Pessoa {id} não encontrada", 1)
            return marshal(message, message_fields)

        db.session.delete(pessoa)
        db.session.commit()

        message = Message("Pessoa deletada com sucesso!", 3)
        return marshal(message, message_fields), 200