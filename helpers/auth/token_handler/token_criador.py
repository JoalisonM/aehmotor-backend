from datetime import datetime, timedelta
from model.pessoa import*
import jwt
import time

class TokenCriador:
    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min:int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min


    def create(self,id:int):
        return self.__encode_token(id)

    def refresh(self, token: str):

        token_informacao = jwt.decode(token,key='1234',algorithms="HS256")
        exp_time =  token_informacao["exp"]

        if (exp_time - time.time()) /60 < self.__REFRESH_TIME_MIN:
            return self.__enconde_token(id)
        return token

    def __encode_token(self,id:int):
       token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=25),
            'id': id
        }, key='1234',algorithm="HS256")

       return token