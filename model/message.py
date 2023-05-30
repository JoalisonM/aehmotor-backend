from flask_restful import fields

message_fields = {
  'cod': fields.Integer,
  'description': fields.String,
}


class Message():
  def __init__(self, description, cod):
    self.cod = cod
    self.description = description