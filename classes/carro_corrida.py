class CarroCorrida:
    def __init__(self, numero:int, piloto:str, velocidadeMaxima:int):
            self.__numero = numero
            self.__piloto = piloto
            self.__velocidadeMaxima = velocidadeMaxima
            self.__velocidadeAtual = 0
            self.__ligado = False
        
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
    
    def acelerar(self, velocidade:int):
        if self.__ligado:
            if self.__velocidadeMaxima < velocidade:
                self.__velocidadeAtual = self.__velocidadeMaxima
            else:
                self.__velocidadeAtual = velocidade
        else:
            print('Ligue o carro para poder acelerar')
    def frear(self):
        self.__velocidadeAtual = 0

    def get_velocidade_atual(self):
        return self.__velocidadeAtual
    
    def get_ligado(self):
        return self.__ligado
# Programa Principal

carro16 = CarroCorrida(16, 'Charles Leclerc', 400)
carro16.ligar()
print(f'O carro está ligado? {carro16.get_ligado()}')
carro16.acelerar(420)
print(f'Velocidade atual: {carro16.get_velocidade_atual()}')
carro16.frear()
print(f'Velocidade atual: {carro16.get_velocidade_atual()}')
carro16.desligar()
print(f'O carro está ligado? {carro16.get_ligado()}')
