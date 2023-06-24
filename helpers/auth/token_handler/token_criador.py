from datetime import datetime, timedelta
from model.pessoa import*
import jwt
import time

class TokenCriador:
    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min:int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min


    def create(self,tipo:str):
        return self.__encode_token(tipo)

    def refresh(self, token: str):

        token_informacao = jwt.decode(token,key = self.__TOKEN_KEY, algorithms="HS256")
        tipo = token_informacao["tipo"]
        exp_time =  token_informacao["exp"]

        if ((exp_time - time.time()) /60) < self.__REFRESH_TIME_MIN:
            print(tipo)
            return self.__enconde_token(tipo)
        return token

    def __encode_token(self,tipo:str):
       token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes = self.__EXP_TIME_MIN),
            'tipo': tipo
        }, key = self.__TOKEN_KEY,algorithm="HS256")

       return token