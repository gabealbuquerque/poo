import datetime

class Perfil:
    def __init__(self, nome:str, sobrenome:str, data_nascimento:str, email:str, telefone:str, sexo:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = telefone
        self.sexo = sexo
        
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'    

    def exibePerfil(self):
        print(f'\nInformações do seu perfil:\n \nNome: {self.nome}\nSobrenome: {self.sobrenome}\nData de Nascimento: {self.data_nascimento}\nEmail: {self.email}\nNúmero de telefone: {self.celular}\nSexo: {self.sexo}')


class Postagem:
    def __init__(self, perfil, texto):
        self.perfil = perfil
        self.texto = texto
    
    def exibePostagem(self):
         return f'{self.perfil.nome_completo()} \n{self.texto()}'
