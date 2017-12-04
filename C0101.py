import math


class PoligonoReg():
        def __init__(self,tamanhoLado, numeroLados):
                self.tamanhoLado,self.numeroLados = tamanhoLado,numeroLados
        def perimetro(self):
                return self.numeroLados * self.tamanhoLados
        def anguloInterno(self):
                return (self.numeroLados - 2) * 180 / self.numeroLados
        def area(self):
                x = self.anguloInterno() * math.pi / 360
                return math.tan(x) * self.tamanhoLado**2 *self.numeroLados / 4
        

class TrianguloReg(PoligonoReg):
        #listaTriangulos = []
        def __init__(self, tamanhoLado):
                super().__init__(tamanhoLado, 3)
                self.tamanhoLado = tamanhoLado
        def area(self):
                return self.tamanhoLado**2 * math.sqrt(3) / 4
        

class QuadrilateroReg(PoligonoReg):
        listaQuadrilatero = []
        def __init__(self, tamanhoLadoA, tamanhoLadoB):
                super().__init__((tamanhoLadoA + tamanhoLadoB)/2 , 4)
                self.tamanhoLadoA, self.tamanhoLadoB = tamanhoLadoA, tamanhoLadoB
        def area(self):
                return self.tamanhoLadoA * self.tamanhoLadoB
        

class QuadradoReg(PoligonoReg):
        listaQuadrado = []
        def __init__(self, tamanhoLado):
                super().__init__(tamanhoLado, 4)
                self.tamanhoLado = tamanhoLado
        def area(self):
                return self.tamanhoLado**2
        

class PentagonoReg(PoligonoReg):
        listaPentagon = []
        def __init__(self, tamanhoLado):
                super().__init__(tamanhoLado, 5)
                self.tamanhoLado = tamanhoLado


class HexagonReg(PoligonoReg):
        listaHexagono = []
        def __init__(self, tamanhoLado):
                super().__init__(tamanhoLado, 6)
                self.tamanhoLado = tamanhoLado
        

class OctogonoReg(PoligonoReg):
        listaOctogono = []
        def __init__(self, tamanhoLado):
                super().__init__(tamanhoLado, 8)
                self.tamanhoLado = tamanhoLado
