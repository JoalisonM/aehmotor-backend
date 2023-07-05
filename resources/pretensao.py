from flask_restful import Resource, reqparse, marshal
from model.pretensao import *
from model.message import *
from model.viagem import *
from model.rota import *
from model.aluno import *
from helpers.base_logger import logger
from helpers.auth.token_handler.token_verificador import token_verifica
import datetime


parser = reqparse.RequestParser()
parser.add_argument('id_viagem', type=str, help='Problema na viagem', required=True)
parser.add_argument('id_aluno', type=str, help='Problema em aluno', required=True)
parser.add_argument('embarque',type=bool, help= 'Problema em embarque')
parser.add_argument('data_embarque', type=str, help= 'Problema em data de embarque')

class Pretensoes(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Pretensão das viagens listadas com sucesso!")
        pretensoes = Pretensao.query.all()
        return marshal(pretensoes, pretensao_fields), 200

    @token_verifica
    def post(self, refresh_token,token_tipo):
        args = parser.parse_args()
        try:

            id_viagem =  args["id_viagem"]
            id_aluno = args["id_aluno"]
            embarque = args["embarque"]
            data_embarque = args["data_embarque"]

            pretensao = Pretensao(id_viagem, id_aluno, embarque, data_embarque)

            db.session.add(pretensao)
            db.session.commit()

            logger.info("Pretensão da id_viagem cadastrada com sucesso!")

            return marshal(pretensao, pretensao_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar", 2)
            return marshal(message, message_fields), 404

class PretensaoById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        pretensao = Pretensao.query.get(id)

        if pretensao is None:
            logger.error(f"Pretensão de viagem {id} não encontrada")

            message = Message(f"Pretensão de viagem {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Pretensão de viagem  {id} encontrada com sucesso!")
        return marshal(pretensao, pretensao_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            pretensao = Pretensao.query.get(id)

            if pretensao is None:
                logger.error(f"Pretensão de viagem  {id} não encontrada")
                message = Message(f"Pretensão de viagem  {id} não encontrada", 1)
                return marshal(message, message_fields)

            pretensao.id_viagem = args["id_viagem"]
            pretensao.id_aluno = args["id_aluno"]
            pretensao.embarque = args["embarque"]
            pretensao.data_embarque = args["data_embarque"]

            db.session.add(pretensao)
            db.session.commit()

            logger.info("Pretensão de viagem cadastrada com sucesso!")
            return marshal(pretensao, pretensao_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar pretensão de viagem", 2)
            return marshal(message, message_fields), 404

    # @token_verifica
    def patch(self, id):
        try:
            pretensao = Pretensao.query.get(id)

            if pretensao is None:
                logger.error(f"Pretensão de viagem  {id} não encontrada")
                message = Message(f"Pretensão de viagem  {id} não encontrada", 1)
                return marshal(message, message_fields)

            pretensao.embarque = 1

            db.session.add(pretensao)
            db.session.commit()

            logger.info("Confirmação de viagem cadastrada com sucesso!")
            return marshal(pretensao, pretensao_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar confirmação de viagem", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token,token_tipo, id):
        pretensao = Pretensao.query.get(id)

        if pretensao is None:
            logger.error(f"Pretensão de viagem {id} não encontrada")
            message = Message(f"Pretensão de viagem {id} não encontrada", 1)
            return marshal(message, message_fields)

        db.session.delete(pretensao)
        db.session.commit()

        message = Message("Pretensão de viagem deletada com sucesso!", 3)
        return marshal(message, message_fields), 200