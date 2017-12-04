class NaoFibonachi(Exception):
    def __init__(self):
        super().__init__("Não é um numero de Fibonachi")

class ListaDeFibonachi(list):
    
    def __init__(self):
        super().__init__(self)
        self.lista = []
        self.i = 1
        self.j = 1
        self.k = 1
        
    def adiciona(self,numero):
        try:
            while(not ((numero < self.i or numero < self.j)or(numero == self.i or numero == self.j))):
                self.k = self.j
                self.i = self.i + self.j
                self.j = self.i + self.j
            if numero != self.i and numero != self.j:
                raise NaoFibonachi
            else:
                list.append(self, numero)
                
                        
        except NaoFibonachi as de:
            if(self.i > numero):
                if(numero - self.k > self.i - numero):
                    list.append(self, self.i)
                else:
                    list.append(self, self.k)
            else:
                if(numero - self.i > self.j - numero):
                    list.append(self, self.j)
                else:
                    list.append(self, self.i)
            return "Erro {0}".format(de.args)



