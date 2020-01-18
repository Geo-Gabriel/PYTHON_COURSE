def exportar_txt(lst_pessoas):
    
    with open('AULA_34/pessoas2.txt', 'a') as arquivo:
        for p in lst_pessoas:
            arquivo.write(f"{p['ID']};{p['NOME']};{p['SOBRENOME']};{p['IDADE']};{p['ENDEREÇO']} \n")
            