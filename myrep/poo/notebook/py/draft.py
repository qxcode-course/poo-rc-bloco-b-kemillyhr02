class Notebook:
    def __init__(self):
        self.__ligado: bool= False
        self.__bateria: Bateria| None=None

    def __str__(self)-> str:
        return f"ligar: {self.__ligado} bateria: {self.__bateria}"

    def ligar(self):
        if self.__ligado:
            print(f"Notebook ligado")
        else :
            print(f"Notebook desligado")
    def usar(self, tempo: int):
        if tempo>self.__bateria:
            
    


class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int= capacidade 
    
