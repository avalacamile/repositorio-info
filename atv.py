class Teste:
     def __init__(self, nome, idade, cpf, familia):
      self.nome = nome
      self.idade = idade
      self.__familia = familia
      self.__cpf = cpf

     def correr(self):
       print('Estou correndo')   

     def beber(self, bebida):
        if bebida == 'cerveja':
           self.__apresentar_documento()
        print('bebendo...')

     def __apresentar_documento(self):
        print(self.__cpf)

pessoa = Teste('Ana',32,'145.098.647-32','Souza')
pessoa.beber ('cerveja')
pessoa.beber ('coca-cola')
   

    


