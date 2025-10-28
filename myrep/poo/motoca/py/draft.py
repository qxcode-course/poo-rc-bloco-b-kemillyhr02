class Pessoa:
        def __init__(self, nome: str, idade: int):
         self.nome = nome
         self.idade = idade
                                
        def __str__(self):
         return f"{self.nome}:{self.idade}"

        def get_idade(self):
         return self.idade
class Moto: 
        def __init__(self):
          self.__pessoa: Pessoa =""
          self.__potencia: int = 1
          self.__tempo: int = 0
                                                                                            
        def __str__(self):
         pessoa = self.__pessoa 
         if self.__pessoa != "":
    
          return f"power:{self.__potencia}, time:{self.__tempo}, person:({self.__pessoa})"
                                                                                                                                                         
        def get_pessoa(self):
         return self.__pessoa
        def __str__(self):
         return f"{self.nome}:{self.idade}"                                                                                          