class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
     self.__nome = nome
     self.__sobrenome = sobrenome
     self.__cpf = cpf
     self.__renda= renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
     
    
class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
     self.__nome = nome
     self.__sobrenome = sobrenome
     self.__cpf = cpf
     self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
   
    
cliente1 = Cliente('Ana', 'Eloisa','123.123.123.12', 10.000)
funcionario1 = Funcionario('Maria', 'das Dores','432.789.098.12', 18976)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())
    


