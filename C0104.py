from tkinter import *
from tkinter import ttk

class Calculadora():
    def __init__(self):
        self.num1, self.num2, self.operação, self.operador = "0", "0", "", "+"
        self.root = Tk()
        
        self.root.title("Calculadora")

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.conta = StringVar()
        self.strConta = ""
        self.resposta = StringVar()
        self.strResposta = ""
        self.segundoNum = False
        self.segundoOpe = False

        ttk.Label(self.mainframe, textvariable=self.conta).grid(column=1, row=0, columnspan=2)
        ttk.Label(self.mainframe, text="=").grid(column=3, row=0)
        ttk.Label(self.mainframe, textvariable=self.resposta).grid(column=4, row=0)

        ttk.Button(self.mainframe, text="1", command=self.teclaNumero1).grid(column=1, row=1)
        ttk.Button(self.mainframe, text="2", command=self.teclaNumero2).grid(column=2, row=1)
        ttk.Button(self.mainframe, text="3", command=self.teclaNumero3).grid(column=3, row=1)
        ttk.Button(self.mainframe, text="4", command=self.teclaNumero4).grid(column=1, row=2)
        ttk.Button(self.mainframe, text="5", command=self.teclaNumero5).grid(column=2, row=2)
        ttk.Button(self.mainframe, text="6", command=self.teclaNumero6).grid(column=3, row=2)
        ttk.Button(self.mainframe, text="7", command=self.teclaNumero7).grid(column=1, row=3)
        ttk.Button(self.mainframe, text="8", command=self.teclaNumero8).grid(column=2, row=3)
        ttk.Button(self.mainframe, text="9", command=self.teclaNumero9).grid(column=3, row=3)
        ttk.Button(self.mainframe, text="0", command=self.teclaNumero0).grid(column=2, row=4)

        ttk.Button(self.mainframe, text="+", command=self.soma).grid(column=4, row=1)
        ttk.Button(self.mainframe, text="-", command=self.subtração).grid(column=4, row=2)
        ttk.Button(self.mainframe, text="*", command=self.multiplicação).grid(column=4, row=3)
        ttk.Button(self.mainframe, text="/", command=self.divisão).grid(column=4, row=4)

        ttk.Button(self.mainframe, text="Calcular", command=self.operar).grid(column=3, row=4)
        ttk.Button(self.mainframe, text="Limpar", command=self.limpar).grid(column=1, row=4)

        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.root.mainloop()


    def operar(self):
        if(self.operador == "+"):
            print(self.num1,self.num2)
            x = int(self.num1) + int(self.num2)
            self.resposta.set(str(x))

        if(self.operador == "-"):
            x = int(self.num1) - int(self.num2)
            self.resposta.set(str(x))

        if (self.operador == "*"):
            x = int(self.num1) * int(self.num2)
            self.resposta.set(str(x))

        if (self.operador == "/"):
            x = int(self.num1) / int(self.num2)
            self.resposta.set(str(x))

    def limpar(self):
        self.num1, self.num2, self.operação, self.operador = "0", "0", "", "+"
        self.conta.set("")
        self.resposta.set("")
        self.segundoNum = False
        self.segundoOpe = False


    def teclaNumero1(self):
        if(self.segundoNum):
            self.num2 += "1"
            self.operação += "1"
            self.conta.set(self.operação)
        else:
            self.num1 += "1"
            self.operação += "1"
            self.conta.set(self.operação)

    def teclaNumero2(self):
        if (self.segundoNum):
            self.num2 += "2"
            self.operação += "2"
            self.conta.set(self.operação)
        else:
            self.num1 += "2"
            self.operação += "2"
            self.conta.set(self.operação)

    def teclaNumero3(self):
        if (self.segundoNum):
            self.num2 += "3"
            self.operação += "3"
            self.conta.set(self.operação)
        else:
            self.num1 += "3"
            self.operação += "3"
            self.conta.set(self.operação)

    def teclaNumero4(self):
        if (self.segundoNum):
            self.num2 += "4"
            self.operação += "4"
            self.conta.set(self.operação)
        else:
            self.num1 += "4"
            self.operação += "4"
            self.conta.set(self.operação)

    def teclaNumero5(self):
        if (self.segundoNum):
            self.num2 += "5"
            self.operação += "5"
            self.conta.set(self.operação)
        else:
            self.num1 += "5"
            self.operação += "5"
            self.conta.set(self.operação)
    def teclaNumero6(self):
        if (self.segundoNum):
            self.num2 += "6"
            self.operação += "6"
            self.conta.set(self.operação)
        else:
            self.num1 += "6"
            self.operação += "6"
            self.conta.set(self.operação)

    def teclaNumero7(self):
        if (self.segundoNum):
            self.num2 += "7"
            self.operação += "7"
            self.conta.set(self.operação)
        else:
            self.num1 += "7"
            self.operação += "7"
            self.conta.set(self.operação)

    def teclaNumero8(self):
        if (self.segundoNum):
            self.num2 += "8"
            self.operação += "8"
            self.conta.set(self.operação)
        else:
            self.num1 += "8"
            self.operação += "8"
            self.conta.set(self.operação)

    def teclaNumero9(self):
        if (self.segundoNum):
            self.num2 += "9"
            self.operação += "9"
            self.conta.set(self.operação)
        else:
            self.num1 += "9"
            self.operação += "9"
            self.conta.set(self.operação)

    def teclaNumero0(self):
        if (self.segundoNum):
            self.num2 += "0"
            self.operação += "0"
            self.conta.set(self.operação)
        else:
            self.num1 += "0"
            self.operação += "0"
            self.conta.set(self.operação)

    def soma(self):
        if(self.segundoOpe):
            self.conta.set("Não pode usar dois operadores")
        else:
            self.segundoOpe = True
            self.operador = "+"
            self.operação += "+"
            self.conta.set(self.operação)
            self.num1 = int(self.num1)
            self.segundoNum = True

    def subtração(self):
        if (self.segundoOpe):
            self.conta.set("Não pode usar dois operadores")
        else:
            self.segundoOpe = True
            self.operador = "-"
            self.operação += "-"
            self.conta.set(self.operação)
            self.num1 = int(self.num1)
            self.segundoNum = True

    def multiplicação(self):
        if (self.segundoOpe):
            self.conta.set("Não pode usar dois operadores")
        else:
            self.segundoOpe = True
            self.operador = "*"
            self.operação += "*"
            self.conta.set(self.operação)
            self.num1 = int(self.num1)
            self.segundoNum = True

    def divisão(self):
        if (self.segundoOpe):
            self.conta.set("Não pode usar dois operadores")
        else:
            self.segundoOpe = True
            self.operador = "/"
            self.operação += "/"
            self.conta.set(self.operação)
            self.num1 = int(self.num1)
            self.segundoNum = True

cal = Calculadora()
