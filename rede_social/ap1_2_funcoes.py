import datetime

class Perfil:
    def __init__(self, nome:str, sobrenome:str, data_nascimento:str, email:str, telefone:str, sexo:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = telefone
        self.sexo = sexo
        
    def exibePerfil(self):
        print(f'\nInformações do seu perfil:\n \nNome: {self.nome}\nSobrenome: {self.sobrenome}\nData de Nascimento: {self.data_nascimento}\nEmail: {self.email}\nNúmero de telefone: {self.celular}\nSexo: {self.sexo}')


class Postagem:
    def __init__(self, texto:str):
        self.texto = []
        self.texto.append(texto)
        self.comentarios = []
    
    def exibePostagem(self):
        print(f'{self.texto}')
    
    def adicionaComentario(self, comentario:str):
        self.comentarios.append(comentario)

    def exibeComentario(self):
        if self.comentarios:
            for indice, comentario in enumerate(self.comentarios, start=1):
                print(f'{comentario}')
        else:
            print('Seja a primeira pessoa a comentar! ')
