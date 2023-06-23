from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.instituicaoEnsino import *
from model.prefeitura import *
from model.motorista import *
from model.veiculo import *
from model.rota import *
from model.message import *
from helpers.database import db
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('id_motorista', type=str, help='Problema no id do motorista', required=True)
parser.add_argument('id_veiculo', type=str, help='Problema no id do veiculo', required=True)
parser.add_argument('id_instituicao_ensino', type=str, help='Problema no id do instituicao', required=True)
parser.add_argument('id_prefeitura', type=str, help='Problema no id do prefeitura', required=True)
parser.add_argument('cidade_origem', type=str, help='Problema na cidade de origem', required=True)
parser.add_argument('cidade_destino', type=str, help='Problema na cidade de destino', required=True)
parser.add_argument('qtd_alunos', type=str, help='Problema na quantidade de alunos', required=True)
parser.add_argument('horario_saida', type=str, help='Problema no horario da saida', required=True)
parser.add_argument('horario_chegada', type=str, help='Problema no horario da entrada', required=True)



class Rotas(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Ufs listados com sucesso!")
        rotas = Rota.query.all()
        return marshal(rotas, rota_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            id_motorista = args["id_motorista"]
            id_veiculo = args["id_veiculo"]
            id_instituicao_ensino = args["id_instituicao_ensino"]
            id_prefeitura = args["id_prefeitura"]
            cidade_origem = args["cidade_origem"]
            cidade_destino = args["cidade_destino"]
            qtd_alunos = args["qtd_alunos"]
            horario_saida = args["horario_saida"]
            horario_chegada = args["horario_chegada"]

            rota = Rota(id_motorista, id_veiculo, id_instituicao_ensino,
                        id_prefeitura, cidade_origem, cidade_destino,
                        qtd_alunos, horario_saida, horario_chegada
            )

            db.session.add(rota)
            db.session.commit()

            logger.info("Rota cadastrada com sucesso!")

            return marshal(rota, rota_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar a rota", 2)
            return marshal(message, message_fields), 404

class RotaById(Resource):
    @token_verifica
    def get(self, refresh_token,token_tipo, id):
        rota = rota.query.get(id)

        if rota is None:
            logger.error(f"Rota {id} não encontrado")

            message = Message(f"Rota {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Rota {id} encontrado com sucesso!")
        return marshal(rota, rota_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            rota = Rota.query.get(id)

            if rota is None:
                logger.error(f"Rota {id} não encontrado")
                message = Message(f"Rota{id} não encontrado", 1)
                return marshal(message, message_fields)

            rota.id_motorista = args["id_motorista"]
            rota.id_veiculo = args["id_veiculo"]
            rota.id_instituicao_ensino = args["id_instituicao_ensino"]
            rota.id_prefeitura = args["id_prefeitura"]
            rota.cidade_origem = args["cidade_origem"]
            rota.cidade_destino = args["cidade_destino"]
            rota.qtd_alunos = args["qtd_alunos"]
            rota.horario_saida = args["horario_saida"]
            rota.horario_chegada = args["horario_chegada"]

            db.session.add(rota)
            db.session.commit()

            logger.info("Rota cadastrado com sucesso!")
            return marshal(rota, rota_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Uf", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo,id):
        rota = Rota.query.get(id)

        if rota is None:
            logger.error(f"Rota {id} não encontrado")
            message = Message(f"Rota {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(rota)
        db.session.commit()

        message = Message("Rota deletado com sucesso!", 3)
        return marshal(message, message_fields), 200

class RotaByCidadeDestino(Resource):
    def get(self, cidade_destino):
        rota = Rota.query.filter(
            Rota.cidade_destino.ilike(f"%{cidade_destino}%")
        ).all()

        if rota is None:
            logger.error(f"Rota {id} não encontrada")

            message = Message(f"Rota {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Rota {id} encontrada com sucesso!")
        return marshal(rota, rota_fields), 200