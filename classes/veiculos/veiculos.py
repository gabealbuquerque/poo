from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, ano:int, preco:float, motor:str):
        self.ano = ano
        self.preco = preco
        self.motor = motor
    
    @abstractmethod
    def exibirDados():
        pass

class Carro(Veiculo):
    def __init__(self, ano:int, preco:float, motor:str, cor:str, modelo:str):
        super().__init__(ano, preco, motor)
        self.cor = cor
        
    def exibirDados(self):
        print(f'Ano: {self.ano}\nPreço: R$ {self.preco:.2f}\nCor: {self.cor}\nModelo: {self.modelo}.')
    
class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento:float):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento
    
    def exibirDados():
        print(f'')
