import sys

sys.path.append('')
from controller.pessoa_controller import PessoaController

pessoa_c = PessoaController()

for p in pessoa_c.listar_todos():
    print(p)