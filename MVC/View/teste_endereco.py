import sys
sys.path.append("/Users/900139/Desktop/GIT/PYTHON_COURSE/MVC")
from Controller.endereco_controller import EnderecoController
from Model.endereco import Endereco

end = Endereco()
end.rua = 'Rua dos Pombos123'
end.bairro = '0'
end.numero = 'casa muito engraçada'
end.cep = 'sem nome'
end.cidade = 'gaspar'
end.estado = '11111-000'
end.id = 10

contr =  EnderecoController()
id_salvo = contr.salvar(end)
print(contr.buscar_por_id(id_salvo))
