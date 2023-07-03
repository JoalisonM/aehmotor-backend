from flask_restful import fields

tokenFields = {"token":fields.String}
class Token:
    def __init__(self,token):
        self.token = token