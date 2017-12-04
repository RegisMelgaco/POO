class MinhaLista(list):
    def __init__(self):
        super().__init__()
    def append(self, numero):
        if((numero % 3 == 0) & (numero % 5 == 0)):
            super().append(numero)
        else:
            print("numero invalido")
