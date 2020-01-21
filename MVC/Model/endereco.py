class Endereco:
    id = 0
    rua = ''
    bairro = ''
    numero = ''
    cep = ''
    cidade = ''
    estado = ''

    def __str__(self):
        return f'{self.id};{self.rua};{self.bairro};{self.numero};{self.cep};{self.cidade};{self.estado}'
        