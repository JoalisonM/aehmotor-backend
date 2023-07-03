from flask_restful import Resource, reqparse, marshal
from helpers.base_logger import *
from model.rota import *
from model.message import *
from model.instituicaoEnsino import *
from model.rotaInstituicaoEnsino import *
from helpers.auth.token_handler.token_verificador import token_verifica

parser = reqparse.RequestParser()
parser.add_argument('id_rota', type=str, help='Problema na rota', required=True)
parser.add_argument('id_instituicao_ensino', type=str, help='Problema na instituição', required=True)

class RotaInstituicoesDeEnsino(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Rota_Instituição listadas com sucesso!")
        rota_instituicao = RotaInstituicaoEnsino.query.all()
        return marshal(rota_instituicao, rota_instituicao_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        try:
            args = parser.parse_args()
            rota = args["id_rota"]
            id_instituicao_ensino = args["id_instituicao_ensino"]
            rota_instituicao = RotaInstituicaoEnsino(rota, id_instituicao_ensino)

            db.session.add(rota_instituicao)
            db.session.commit()

            logger.info("Rota_Instituição cadastrada com sucesso!")

            return marshal(rota_instituicao, rota_instituicao_fields), 200

        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Uf", 2)
            return marshal(message, message_fields), 404

class RotasInstituicoesDeEnsino(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo,id):
        rota_instituicao = RotaInstituicaoEnsino.query.get(id)

        if rota_instituicao is None:
            logger.error(f"Rota_Instituição {id} não encontrado")

            message = Message(f"Rota_Instituição {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Rota_Instituição {id} encontrado com sucesso!")
        return marshal(rota_instituicao, rota_instituicao_fields)

    @token_verifica
    def put(self, refresh_token,token_tipo,id):
        args = parser.parse_args()

        try:
            rota_instituicao = RotaInstituicaoEnsino.query.get(id)

            if rota_instituicao is None:
                logger.error(f"Rota_Instituição {id} não encontrado")
                message = Message(f"Rota_Instituição {id} não encontrado", 1)
                return marshal(message, message_fields)

            rota_instituicao.nome = args["id_rota"]
            rota_instituicao.sigla = args["id_instituicao_ensino"]

            db.session.add(rota_instituicao)
            db.session.commit()

            logger.info("Rota_Instituição cadastrado com sucesso!")
            return marshal(rota_instituicao, rota_instituicao_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Rota_Instituição", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, id):
        rota_instituicao = RotaInstituicaoEnsino.query.get(id)

        if rota_instituicao is None:
            logger.error(f"Rota_Instituição {id} não encontrado")
            message = Message(f"Rota_Instituição {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(rota_instituicao)
        db.session.commit()

        message = Message("Rota_Instituição deletado com sucesso!", 3)
        return marshal(message, message_fields), 200