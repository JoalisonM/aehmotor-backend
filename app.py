import os
from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask, Blueprint


from helpers.cors import cors
from helpers.database import db, migrate
from resources.motorista import Motoristas, MotoristaById, MotoristaByNome
from resources.veiculo import Veiculos, VeiculoById, VeiculoByNome
from resources.passageiro import Passageiros, PassageiroById
from resources.cidade import Cidades,CidadeById, CidadeByNome
from resources.endereco import Enderecos, EnderecoById, EnderecoByNome
from resources.aluno import Alunos, AlunoById, AlunoByNome
from resources.pessoa import Pessoas, PessoaById, PessoaByNome
from resources.uf import Ufs, UfById, UfByNome
from resources.instituicaoEnsino import InstituicoesDeEnsino, InstituicaoDeEnsinoById, InstituicaoDeEnsinoByNome
from resources.funcionario import Funcionarios, FuncionarioById, FuncionarioByNome
from resources.rota import Rotas, RotaById, RotaByNome
from resources.prefeitura import Prefeituras, PrefeituraById
from resources.notificacao import EnviarEmailResource


load_dotenv()

# create the app
app = Flask(__name__)

# restful
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api")

postgresUser = os.getenv("POSTGRES_USER")
postgresPassword = os.getenv("POSTGRES_PASSWORD")

DB_URL = f"postgresql://{postgresUser}:{postgresPassword}@localhost:5432/aehmotor"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# initialize the app with the extension
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)


api.add_resource(Motoristas,'/motoristas')
api.add_resource(MotoristaById,'/motoristas/<int:id>')
api.add_resource(MotoristaByNome,'/motoristas/<nome>')
api.add_resource(Veiculos,'/veiculos')
api.add_resource(VeiculoById,'/veiculos/<int:id>')
api.add_resource(VeiculoByNome,'/veiculos/<nome>')
api.add_resource(Passageiros, '/passageiros')
api.add_resource(PassageiroById,'/passageiros/<int:id>')
api.add_resource(Alunos, '/alunos')
api.add_resource(AlunoById, '/alunos/<int:idPessoa>')
api.add_resource(AlunoByNome,'/alunos/<nome>')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(PessoaById, '/pessoas/<int:id>')
api.add_resource(PessoaByNome,'/pessoas/<nome>')
api.add_resource(Cidades,'/cidades')
api.add_resource(CidadeById,'/cidades/<int:id>')
api.add_resource(CidadeByNome,'/cidades/<nome>')
api.add_resource(Enderecos,'/enderecos')
api.add_resource(EnderecoById,'/enderecos/<int:id>')
api.add_resource(EnderecoByNome,'/enderecos/<nome>')
api.add_resource(Ufs, '/ufs')
api.add_resource(UfById, '/ufs/<int:id>')
api.add_resource(UfByNome,'/ufs/<nome>')
api.add_resource(InstituicoesDeEnsino, '/instituicoesDeEnsino')
api.add_resource(InstituicaoDeEnsinoById, '/instituicoesDeEnsino/<int:id>')
api.add_resource(InstituicaoDeEnsinoByNome,'/instituicoesDeEnsino/<nome>')
api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(FuncionarioById, '/funcionarios/<int:id>')
api.add_resource(FuncionarioByNome,'/funcionarios/<nome>')
api.add_resource(Rotas, '/rotas')
api.add_resource(RotaById, '/rotas/<int:id>')
api.add_resource(RotaByNome,'/rotas/<nome>')
api.add_resource(Prefeituras, '/prefeituras')
api.add_resource(PrefeituraById, '/prefeituras/<int:id>')
api.add_resource(EnviarEmailResource, '/enviar_email')



# Blueprints para Restful
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
