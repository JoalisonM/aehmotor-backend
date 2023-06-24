from flask_restful import fields

login_fields = {
  'token': fields.String
}


class LoginModel():
  def __init__(self, token):
    self.token = token
