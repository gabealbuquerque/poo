import datetime

class RedeSocial: # classe chamada rede social a qual o def init é a criação de perfil
    def __init__(self, nome:str, sobrenome:str, email:str, celular:str, data_nasc:str, sexo: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.celular = celular
        self.data_nascimento = data_nasc
        self.sexo = sexo

    # metódo que permite adicionar amigos pelo nome completo
    def adicionar_amigos(self, nome_completo:str):
        self.adicionar_amigos = nome_completo

    # metódo que permite criar postagem com um texto
    def criar_postagem(self, texto:str):
        self.criar_postagem = texto

    # metódo que permite comentár na postagem por meio de comentário 
    def comentar_postagem(self, comentario:str):
        self.comentar_postagem = comentario
