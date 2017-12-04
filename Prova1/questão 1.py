class Quadrado():
    def __init__(self,tamLado):
        self.tamLado = tamLado
    def area(self):
        return self.tamLado * self.tamLado

class CoroaQuadrada(Quadrado):
    def __init__(self,ladoFigura,ladoFuro):
        super().__init__(ladoFigura)
        self.ladoFuro = ladoFuro
    def areaComFuro(self):
        return (self.area() - (self.ladoFuro * self.ladoFuro))
        
        
