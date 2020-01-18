from def_pessoa_db import listar_todos
from def_pessoa_convert import converter_tabela_dic
from def_pessoa_export import exportar_txt

lpt = listar_todos()

lpd = converter_tabela_dic(lpt)

exportar_txt(lpd)
