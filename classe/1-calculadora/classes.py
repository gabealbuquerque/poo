class Comprimento:
    def __init__(self, opcao:int):
        self.opcao = opcao
    
        if self.opcao == 1:
            self.MetrosParaCentimetro()

    def MetrosParaCentimetro(self, metros:float):
        self.metros = metros
        print(f'\n{self.metros:.2f} (m) é igual a {self.metros * 100:.2f} (cm)\n')
    
    def CentimetroParaMetro(self, centimetro:float):
        self.centimetro = centimetro
        print(f'{self.centimetro:.2f} (cm) é igual a {self.centimetro / 100:.2f} (m)')


class Calculadora:
    def __init__(self, opcao:int, numero1:float, numero2:float):
        self.opcao = opcao
        self.numero1 = numero1
        self.numero2 = numero2

        if self.opcao == 1:
            self.soma()
        elif self.opcao == 2:
            self.subtracao()
        elif self.opcao == 3:
            self.multiplicacao()
        elif self.opcao == 4:
            self.divisao()
          
    def soma(self):
        print(f'\n{self.numero1} + {self.numero2} = {self.numero1 + self.numero2}')

    def subtracao(self):
        print(f'\n{self.numero1} - {self.numero2} = {self.numero1 - self.numero2}')

    def multiplicacao(self):
        print(f'\n{self.numero1} x {self.numero2} = {self.numero1 * self.numero2}')

    def divisao(self):
        print(f'\n{self.numero1} / {self.numero2} = {self.numero1 / self.numero2}')

