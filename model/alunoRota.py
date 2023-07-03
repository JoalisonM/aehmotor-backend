from flask_restful import fields

aluno_rota_fields = {
  'cidade_destino':fields.String,
  'horario_saida':fields.String,
  'horario_chegada':fields.String,
  'turno':fields.String,
  'nome_instituicao_ensino':fields.String
}
