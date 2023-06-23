from flask import request
from helpers.auth.token_handler.token_verificador import token_verifica
from flask_restful import Resource, marshal
from jwt import decode
from datetime import datetime
from model.blackList import BlackList
from model.message import Message, message_fields
from helpers.database import db
from helpers.auth.token_handler.token_verificador import token_verifica

class Logout(Resource):
    @token_verifica
    def post(self, id, token):

        try:
            token_puro = request.headers.get("Authorization")
            #request_data = request.get_json()
            #token_puro = request_data.get('token')
            novo_token = token_puro.split()[1]
            token_informacao = decode(novo_token, key="1234", algorithms="HS256")
            token_exp = token_informacao['exp']

            token_blackList = BlackList(token=novo_token, data_expiracao=datetime.fromtimestamp(token_exp))

            db.session.add(token_blackList)
            db.session.commit()

            message = Message("Logout realizado com sucesso", 0)
            return marshal(message, message_fields), 200

        except IndexError:
            message = Message("Autenticação não realizada.", 1)

            return marshal(message, message_fields), 400
        """except:
            message = Message("Erro no logout", 2)

            return marshal(message, message_fields), 400"""
