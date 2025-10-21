class Camisa:
    def __init__(self):
        self.__tamanho: str =""

    def __str__(self)->str:
        return f"size: ({self.__tamanho})"

    def set_tamanho(self, tam: str):
        if tam=="PP" or tam=="P" or tam=="M" or tam=="G" or tam=="GG" or tam=="XG":
            self.__tamanho=tam
            return
        print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def get_tamamho(self):
        return self.__tamanho
    
def main():
    camisa= Camisa()
    while True:
        line=input()
        print(f"${line}")
        args=line.split()

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(camisa)
        elif args[0]=="size":
            camisa.set_tamanho(args[1])

main()