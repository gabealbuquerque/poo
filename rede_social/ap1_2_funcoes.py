import datetime

class Perfil: # classe de criação de perfil 
    def __init__(self, nome:str, sobrenome:str, email:str, celular:str, data_nasc:str, sexo: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.celular = celular
        self.data_nascimento = data_nasc
        self.sexo = sexo.upper()    

    def exibir_dados(self):
        print(f'\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nEmail: {self.email}\nCelular: {self.celular}\nData de Nascimento: {self.data_nascimento}\nSexo: {self.sexo}')


    # metódo que permite criar postagem com um texto
class criar_postagem:
    def __init__(self, titulo:str, texto:str):
        self.titulo = titulo
        self.texto = texto

    def exibir_postagem(self):
        print(f'Título: {self.titulo}\nPostagem: {self.texto}.')
    # metódo que permite comentár na postagem por meio de comentário 

class comentar_postagem:
        def __init__(self, comentario:str):
            self.comentar_postagem = comentario
        
        def exibir_comentario(self):
            print(f'{self.comentar_postagem}')
            
def adicionar_amigos(self, nome_completo:str):
    self.adicionar_amigos = nome_completo

