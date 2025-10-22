
class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int= capacidade 
    
    def __str__(self)->str:
        return f""
    

class Notebook:
    def __init__(self):
        self.__ligado: bool= False
        self.__bateria: int = 100

    def __str__(self)-> str:
        return f"ligar: {self.__ligado} bateria: {self.__bateria}"

    def ligar(self):
        if self.__ligado:
            print(f"Notebook ja esta ligado")
        else :
            print(f" desligando notebook")
    
    def desligar(self):
        if not self.__ligado:
            print(f" ja esta desligado")
        else :
            print(f"ligando notebook")
    
    def usar(self, tempo: int):
        if tempo>self.__bateria:
            print(f" usado por {self.__bateria}")
            self.__bateria=0
        elif self.__ligado== False:
            print(f"nao pode usar, notebook esta desligado")
        else:
            print(f"usado por {tempo}")
            self.__bateria-=tempo
        
    def mostrar(self):
        if self.__ligado == True:
            print(f" esta ligado")
        else :
            print(f"esta desligado")
def main():
    notebook = Notebook() # criando notebook
    notebook.mostrar()    # msg: Status: Desligado
    notebook.usar(10)     # msg: erro: ligue o notebook primeiro
    notebook.ligar()      # msg: notebook ligado
    notebook.mostrar()    # msg: Status: Ligado
    notebook.usar(10)     # msg: Usando por 10 minutos
    notebook.desligar()   # msg: notebook desligado
main()
    
