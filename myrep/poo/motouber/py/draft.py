class Pessoa:
    def __init__(self, nome:str, money:int):
        self.__nome = nome
        self.__money = money
    
    def __str__(self,)->str:
        return f"{self.__nome}:{self.__money}"
    def get_nome(self):
        return self.__nome
    def set_nome(self, name: str):
        self.__nome=name
    def get_money(self):
        return self.__money
    def set_money(self, money: int):
        self.__money=money

class Moto:
    def __init__(self):
        self.__passageiro = None 
        self.__motorista = None
        self.__custo = 0

    def __str__(self)->str:
        if self.__motorista==None:
            motorista="None"
        else:
            motorista=self.__motorista

        if self.__passageiro==None:
            passageiro="None"
        else:
            passageiro=self.__passageiro    
        return f"Cost: {self.__custo}, Driver: {motorista}, Passenger: {passageiro}"
    
    def setDrive(self, name: str, money: int):
        motorista=Pessoa(name, money)
        if self.__motorista==None:
            self.__motorista= motorista
        else:
            print(f"fail: ja tem um motorista")
    def setPass(self, name: str, money:int):
        passageiro=Pessoa(name, money)
        if self.__passageiro==None:
            self.__passageiro=passageiro
        else:
            print(f"fail: ja tem um passageiro")

    def drive(self, n:int):
        self.__custo+=n

    def leavePass(self):
        if self.__passageiro.get_money()<self.__custo:
            print("fail: Passenger does not have enough money")
            self.__passageiro.set_money(0)

        else:
            self.__passageiro.set_money(self.__passageiro.get_money()-self.__custo)
            
        print(f"{self.__passageiro} left")
        self.__motorista.set_money(self.__motorista.get_money()+self.__custo)
        self.__passageiro=None
        self.__custo=0

def main():
    moto=Moto()
    while True:
        line=input()
        print(f"${line}")
        args=line.split()
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(moto)
        elif args[0]=="setDriver":
            moto.setDrive(args[1],int(args[2]))
        elif args[0]=="setPass":
            moto.setPass(args[1],int(args[2]))
        elif args[0]=="leavePass":
            moto.leavePass()
        elif args[0]=="drive":
            moto.drive(int(args[1]))
        else :
            print(f"comando invalido")

main()