rua = None

def vazio(dado):
    if dado:
        return dado
    else:
        return ''

print(vazio(rua))
#---- IF ternário em Python
dado = rua if rua else ''
print( dado)