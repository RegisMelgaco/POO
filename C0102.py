import math
class Racional:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    def __str__(self):
        return str(self.dividendo) + '/' + str(self.divisor)
    def __mul__(self, outro):
        divisor = self.divisor*outro.divisor
        dividendo = self.dividendo*outro.dividendo
        return Racional(dividendo, divisor)
    def mmc(self,outro):
        divCom = self.divisor*outro.divisor
        self.dividendo*=outro.divisor
        outro.dividendo*=self.divisor
        self.divisor,outro.divisor = divCom, divCom
        i = 2
        print("a=", a)
        print("b=", b)
        while((i <= self.divisor/2) & (i <= outro.divisor/2)):
            if((self.dividendo%i == 0) & (outro.dividendo%i == 0) & (self.divisor%i == 0)):
                self.dividendo = int(self.dividendo/i)
                outro.dividendo = int(outro.dividendo/i)
                self.divisor,outro.divisor = int(self.divisor/i), int(self.divisor/i)
                print("a=", a)
                print("b=", b)
            else:
                i+=1
        return Racional(self.dividendo, self.divisor)
    def __add__(self,outro):
        self.mmc(outro)
        outro.mmc(self)
        self.dividendo = self.dividendo + outro.dividendo
        return Racional(self.dividendo, self.divisor)
    def __sub__(self,outro):
        self.mmc(outro)
        outro.mmc(self)
        self.dividendo = self.dividendo - outro.dividendo
        return Racional(self.dividendo, self.divisor)
    def __div__(self,outro):
        self.divisor = self.divisor*outro.dividendo
        self.dividendo = self.dividendo*outro.divisor
        return Racional(self.dividendo, self.divisor)
    def __abs__(self):
        if(self.divisor < 0):
            self.divisor = -self.divisor
        if(self.dividendo < 0):
            self.dividendo = -self.dividendo
        return Racional(self.dividendo, self.divisor)
    def __neg__(self):
        if(self.divisor < 0):
            self.divisor = -self.divisor
        if(self.dividendo >= 0):
            self.dividendo = -self.dividendo
        return Racional(self.dividendo, self.divisor)
    def __pos__(self):
        return self.__abs__()

a = Racional(-5, 10)
b = Racional(1, 4)
