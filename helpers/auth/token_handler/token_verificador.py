from functools import wraps
from flask import jsonify, request
from flask_restful import marshal
import jwt
from model.message import Message,message_fields
from helpers.auth.token_handler.token_singleton import token_criador

def token_verifica(function: callable) -> callable:

    @wraps(function)
    def decorated(*args, **kwargs):
        token_puro = request.headers.get("Authorization")


        if not token_puro:
            messageAl = Message("Login não autorizado",2)

            return marshal(messageAl,message_fields), 400

        try:
            token = token_puro.split()[1]
            token_informacao = jwt.decode(
                token, key='1234', algorithms="HS256")
            token_id = token_informacao["id"]

        except jwt.InvalidSignatureError:
            return jsonify({'error': 'Token inválido'}), 400

        except jwt.ExpiredSignatureError:
            return jsonify({
                'error': 'Token expirado'
            }), 401

        except KeyError as e:
            return jsonify({
                'error': 'Token inválido (2)'
            }), 401


        next_token = token_criador.refresh(token)
        return function( *args, next_token, **kwargs)

    return  decorated