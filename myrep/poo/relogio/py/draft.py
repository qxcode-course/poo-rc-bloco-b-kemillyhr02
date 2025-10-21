class Watch:
    def __init__(self, hora: int = 0 , mini:int= 0, seg:int= 0):
        self.__hora: int = 0
        self.__mini: int = 0
        self.__seg: int = 0
        self.set_hora(hora)
        self.set_min(mini)
        self.set_segundo(seg)

        
    def __str__(self)->str:
        return f"{self.__hora:02}:{self.__mini:02}:{self.__seg:02}"

    def set_hora(self, hora:int):
        if hora>=0 and hora<=23:
            self.__hora=hora
            return
        print(f"fail: hora invalida")

    def set_min(self, mini:int):
        if mini>=0 and mini<=59:
            self.__mini=mini
            return
        print(f"fail: minuto invalido")

    def set_segundo(self, segundo:int):
        if segundo>=0 and segundo<=59:
            self.__seg=segundo
            return
        print(f"fail: segundo invalido")

    def nextSecond(self):
        self.__seg+=1
        if self.__seg>59:
            self.__seg=0
            self.__mini+=1
        if self.__mini>59:
            self.__mini=0
            self.__hora+=1
        if self.__hora>23:
            self.__hora=0

def main():
    watch=Watch()
    while True:
        line=input() 
        print(f"${line}")   
        args=line.split()
        if args[0]=="end":
            break
        elif args[0]=="init":
            watch=Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0]=="show":
            print(watch)
        elif args[0]=="next":
            watch.nextSecond()
        elif args[0]=="set":
            watch.set_hora(int(args[1]))
            watch.set_min(int(args[2]))
            watch.set_segundo(int(args[3]))
main()
    
