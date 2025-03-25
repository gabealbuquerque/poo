from abc import ABC, abstractmethod
class TesouroDireto(ABC):
    def __init__(self, titulo: str, tempo: int, valor: float, taxa: float):
        self.titulo = titulo
        self.tempo = tempo
        self.valor = valor
        self.taxa = taxa

    @abstractmethod
    def simular(self):
        pass


class TesouroPrefixado(TesouroDireto):
    def __init__(self, tempo: int, valor: float):
        # A taxa para Tesouro Prefixado já é definida, não precisamos de parâmetro.
        super().__init__('Prefixado', tempo, valor, 14.72 / 100)  # Convertido para decimal (14.72% -> 0.1472)

    def simular(self):
        valor_final = self.valor * (1 + self.taxa) ** self.tempo
        print(f'O valor final para o Tesouro Prefixado será: R$ {valor_final:.2f}')


class TesouroIpca(TesouroDireto):
    def __init__(self, tempo: int, valor: float, variacao_ipca: float):
        # A taxa para Tesouro IPCA+ já é definida, mas o IPCA precisa ser passado como parâmetro
        super().__init__('IPCA+', tempo, valor, 7.90 / 100)  # Convertido para decimal (7.90% -> 0.079)
        self.variacao_ipca = variacao_ipca / 100  # Convertido para decimal

    def simular(self):
        valor_final = self.valor * (1 + self.taxa + self.variacao_ipca) ** self.tempo
        print(f'O valor final para o Tesouro IPCA+ será: R$ {valor_final:.2f}')


class TesouroSelic(TesouroDireto):
    def __init__(self, tempo: int, valor: float):
        # A taxa para Tesouro Selic já é definida
        super().__init__('Selic', tempo, valor, 0.0579 / 100)  # Convertido para decimal (0.0579% -> 0.000579)

    def simular(self):
        valor_final = self.valor * (1 + self.taxa) ** self.tempo
        print(f'O valor final para o Tesouro Selic será: R$ {valor_final:.2f}')

vi = 1000
t = 10

