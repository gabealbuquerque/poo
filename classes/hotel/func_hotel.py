from datetime import date
class Quarto:
    def __init__(self, numero:int, localizacao:int, ocupado=str): # Cria o número, localização e como situação desocupado do quarto
        self.__numero = numero
        self.__localizacao = localizacao
        self.__ocupado = 'disponivel'
    
    def atribuir_hospede(self): # Função que torna a situação do quarto Ocupada
        if self.__ocupado == 'disponivel':
            self.__ocupado = 'ocupado'
    
    def desocupar(self): # Função que torna a situação do quarto Desocupada
        if self.__ocupado == 'ocupado':
            self.__ocupado = 'disponivel'

    def get_quarto(self):   # Função que retorna os valores do quarto (número, localização e situação)
        print(f'\nINFORMAÇÕES DO QUARTO:\n\nNº do quarto: {self.__numero}\nLocalização: {self.__localizacao}\nSituação: {self.__ocupado}')

    def hospede(self, nome:str):    # Cria o hospede
        self.__nome = nome
        self.__quarto = self.__numero
    
    def get_hospede(self): # Retorna infos do hospede
        print(f'\nINFORMAÇÕES DO CLIENTE:\n\nNome: {self.__nome}\nHospedado no quarto de nº: {self.__numero}\nLocalização: {self.__localizacao}\nDia de início: {date.today()}')
    
    def fazer_check_in(self):   # Torna a situação ocupado
        if self.__ocupado =='disponivel':
            self.__ocupado = 'ocupado'
        print('\nFazendo check in...')
        self.get_quarto()
        print(f'Quarto {self.__ocupado} por: {self.__nome}')

    def fazer_check_out(self):      # Torna a situação desocupado
        if self.__ocupado == 'ocupado':
            self.__ocupado = 'disponivel'
        print('\nFazendo check out...')
        self.get_quarto()
        


    


    


    

    

    
    

