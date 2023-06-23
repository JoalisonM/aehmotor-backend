from functools import wraps
from flask_restful import request, marshal
from jwt import InvalidSignatureError, ExpiredSignatureError,decode
from model.message import Message,message_fields
from model.blackList import BlackList
from helpers.auth.token_handler.token_singleton import token_criador
from model.token import Token, tokenFields

def token_verifica(function: callable) -> callable:

    @wraps(function)
    def decorated(*args, **kwargs):
        token_puro = request.headers.get("Authorization")


        if not token_puro:
            message = Message("Login não autorizado",2)
            return marshal(message, message_fields), 400

        try:
            token = token_puro.split()[1]
            token_informacao = decode(
            token, key='1234', algorithms="HS256")
            token_tipo = token_informacao["tipo"]

        except InvalidSignatureError:
            message = Message("Token inválido", 1)

            return marshal(message, message_fields), 400

        except ExpiredSignatureError:
            message = Message("Token de acesso expirado", 2)

            return marshal(message, message_fields), 401

        except KeyError as e:
            message = Message("Token inválido(2)", 2)

            return marshal(message, message_fields), 401

        blackList_token = BlackList.query.filter_by(token = token).first()
        if blackList_token:
            message = Message("Acesso negado.", 0)

            return marshal (message, message_fields), 401

        next_token = token_criador.refresh(token)

        return function( *args, next_token, token_tipo, **kwargs)

    return  decorated

