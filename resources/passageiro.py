from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.passageiro import*
from model.pessoa import*
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('idAluno', type=int, help= 'Problema no id aluno', required=True)
parser.add_argument('cidadeOrigem', type=str, help='Problema no campo cidade de origem', required=True)
parser.add_argument('cidadeDestino', type=str, help='Problema no campo  cidade de destino', required=True)

class Passageiros(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Passageiros listados com sucesso!")
        passageiros = Passageiro.query.all()
        return marshal(passageiros, passageiro_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            idAluno = args["idAluno"]
            cidadeOrigem= args["cidadeOrigem"]
            cidadeDestino = args["cidadeDestino"]

            passageiro = Passageiro(idAluno, cidadeOrigem, cidadeDestino)

            db.session.add(passageiro)
            db.session.commit()

            logger.info("Passageiro cadastrado com sucesso!")

            return marshal(passageiro, passageiro_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastradar passageiro", 2)
            return marshal(message, message_fields), 404

class PassageiroById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo,  id):
        passageiro = Passageiro.query.get(id)

        if passageiro is None:
            logger.error(f"Passageiro {id} não encontrado")

            message = Message(f"Passageiro {id} não encotrado", 1)
            return marshal(message), 404

        logger.info(f"Passageiro {id} encontrado com sucesso!")
        return marshal(passageiro, passageiro_fields), 200

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            passageiro = Passageiro.query.get(id)
            if passageiro is None:
                logger.error(f"Passageiro {id} não encontrado")
                message = Message(f"Passageiro {id} não encontrado", 1)
                return marshal(message, message_fields)

            passageiro.idAluno = args["idAluno"]
            passageiro.cidadeOrigem = args["cidadeOrigem"]
            passageiro.cidadeDestino = args["cidadeDestino"]

            db.session.add(passageiro)
            db.session.commit()

            logger.info("Passageiro cadastrado com sucesso!")
            return marshal(passageiro, passageiro_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar passageiro", 2)
            return marshal(passageiro, passageiro_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, id):
        passageiro = Passageiro.query.get(id)

        if passageiro is None:
            logger.error(f"Passageiro {id} não encontrado")
            message = Message(f"Passageiro {id} não encontrado", 1)
            return marshal (message, message_fields)

        db.session.delete(passageiro)
        db.session.commit()

        message = Message("Passageiro deletada com sucesso!", 3)
        return marshal(message, message_fields), 200