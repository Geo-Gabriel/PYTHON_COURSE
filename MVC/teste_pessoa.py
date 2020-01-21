import sys
sys.path.append('/Users/900139/Desktop/GIT/PYTHON_COURSE/MVC')
from Controller.pessoa_controller import PessoaController
from Model.pessoa import Pessoa

pessoa = Pessoa()
pessoa.nome = 'George '
pessoa.sobrenome = 'Gabriel'
pessoa.idade = 20
pessoa.endereco.rua = 'Rua dos Alfeneiros'
pessoa.endereco.bairro = 'Jardim Brasil'
pessoa.endereco.numero = '25'
pessoa.endereco.cep = '8965-665'
pessoa.endereco.cidade = 'Fantasma'
pessoa.endereco.estado = 'SC'

controller = PessoaController()
id_salvo = controller.salvar(pessoa)


#print(controller.buscar_por_id(0))
