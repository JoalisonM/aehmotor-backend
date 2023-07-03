from flask_restful import Resource, reqparse, marshal
from model.viagem import *
from model.rota import *
from model.veiculo import *
from model.motorista import *
from model.pretensao import *
from model.message import *
from helpers.base_logger import logger
from helpers.auth.token_handler.token_verificador import token_verifica


parser = reqparse.RequestParser()
parser.add_argument('id_rota', type=str, help='Problema no id da rota', required=True)
parser.add_argument('id_veiculo', type=str, help='Problema no id de veículo', required=True)
parser.add_argument('id_funcionario', type=str, help='Problema no id do funcionário', required=True)
parser.add_argument('data_viagem', type=str, help='Problema na data da viagem', required=True)

class Viagens(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Viagens listadas com sucesso!")
        viagens = Viagem.query.all()
        return marshal(viagens, viagem_fields), 200

    @token_verifica
    def post(self, refresh_token,token_tipo):
        args = parser.parse_args()
        try:

            id_rota = args["id_rota"]
            id_veiculo = args["id_veiculo"]
            id_funcionario = args["id_funcionario"]
            data_viagem = args["data_viagem"]

            viagem = Viagem(id_rota, id_funcionario, id_veiculo, data_viagem)

            db.session.add(viagem)
            db.session.commit()

            logger.info("Viagem cadastrada com sucesso!")

            return marshal(viagem, viagem_fields), 201
        except Exception as e:
                logger.error(f"error: {e}")

                message = Message("Erro ao cadastrar viagem", 2)
                return marshal(message, message_fields), 404

class ViagemById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        viagem = Viagem.query.get(id)

        if viagem is None:
            logger.error(f"Viagem {id} não encontrada")

            message = Message(f"Viagem {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Viagem {id} encontrada com sucesso!")
        return marshal(viagem, viagem_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            viagem = Viagem.query.get(id)

            if viagem is None:
                logger.error(f"Viagem {id} não encontrada")
                message = Message(f"Viagem {id} não encontrada", 1)
                return marshal(message, message_fields)

            viagem.id_rota = args["id_rota"]
            viagem.id_funcionario = args["id_funcionario"]
            viagem.id_veiculo = args["id_veiculo"]
            viagem.data_viagem = args["data_viagem"]


            db.session.add(viagem)
            db.session.commit()

            logger.info("Viagem cadastrada com sucesso!")
            return marshal(viagem, viagem_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar viagem", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token,token_tipo, id):
        viagem = Viagem.query.get(id)

        if viagem is None:
            logger.error(f"Viagem {id} não encontrada")
            message = Message(f"Viagem {id} não encontrada", 1)
            return marshal(message, message_fields)

        db.session.delete(viagem)
        db.session.commit()

        message = Message("Viagem deletada com sucesso!", 3)
        return marshal(message, message_fields), 200


class ViagemById(Resource):
    def get(self, nome):
        viagem = Viagem.query.filter_by(id=id).all()

        if viagem is None:
            logger.error(f"Viagem {id} não encontrada")

            message = Message(f"Viagem {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Viagem {id} encontrada com sucesso!")
        return marshal(viagem, viagem_fields), 200