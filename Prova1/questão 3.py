class inutil():
    def soma(self):
        return 1+1

class inutilFilha(inutil):
    def __init__(self):
        super().__init__()
    def soma(self):
        return 2+2
        
