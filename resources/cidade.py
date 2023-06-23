from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.cidade import*
from model.endereco import *
from model.uf import *
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('sigla', type=str, help='Problema na sigla', required=True)
parser.add_argument('idUf', type=int, help='Problema no id da UF', required=True)


class Cidades(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Cidades listadas com sucesso!")
        cidades = Cidade.query.all()
        return marshal(cidades, cidade_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            sigla = args["sigla"]
            idUf = args["idUf"]


            cidade = Cidade(nome, sigla, idUf)

            db.session.add(cidade)
            db.session.commit()

            logger.info("Cidade cadastrada com sucesso!")

            return marshal(cidade, cidade_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar cidade", 2)
            return marshal(message, message_fields), 404

class CidadeById(Resource):
    @token_verifica
    def get(self,refresh_token, token_tipo, id):
        cidade = Cidade.query.get(id)

        if cidade is None:
            logger.error(f"Cidade {id} não encontrada")

            message = Message(f"Cidade {id} não encontrada", 1)
            return marshal(message), 404

        logger.info(f"Cidade {id} encontrada com sucesso!")
        return marshal(cidade, cidade_fields), 200

    @token_verifica
    def put(self, refresh_token, token_tipo,id):
        args = parser.parse_args()

        try:
            cidade = Cidade.query.get(id)
            if cidade is None:
                logger.error(f"Cidade {id} não encontrada")
                message = Message(f"Cidade {id} não encontrada", 1)
                return marshal(message, message_fields)

            cidade.nome = args["nome"]
            cidade.sigla = args["sigla"]
            cidade.idUf = args["idUf"]

            db.session.add(cidade)
            db.session.commit()

            logger.info("Cidade cadastrada com sucesso!")
            return marshal(cidade, cidade_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar cidade", 2)
            return marshal(cidade, cidade_fields), 404

    @token_verifica
    def delete(self,refresh_token, token_tipo, id):
        cidade = Cidade.query.get(id)

        if cidade is None:
            logger.error(f"Cidade {id} não encontrada")
            message = Message(f"Cidade {id} não encontrada", 1)
            return marshal (message, message_fields)

        db.session.delete(cidade)
        db.session.commit()

        message = Message("Cidade deletada com sucesso!", 3)
        return marshal(message, message_fields), 200