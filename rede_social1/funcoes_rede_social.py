class RedeSocial:
    def __init__(self, user:str, nome:str, sobrenome:str, data_nascimento:str, num_telefone:str, email:str, sexo:str):
        self.user = user
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.numero_telefone = num_telefone
        self.email = email
        self.sexo = sexo
    
    def exibe_perfil(self):
        print(f'\nInformações do Perfil de {self.nome} {self.sobrenome}: ')
        print(f'\nUsername: {self.user}\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nData de Nascimento: {self.data_nascimento}\nNúmero de celular: {self.numero_telefone}\nEmail: {self.email}\nSexo: {self.sexo}')

    def criar_postagem(self, texto:str):
        self.texto = texto

    def exibe_postagem(self):
        print('\nNovas publicações: ')
        print(f'\n{self.nome} {self.sobrenome}\n{self.texto}')

    def criar_comentario(self, comentario:str):
        self.comentario = comentario

    def exibe_cometario(self):
        print('\nNovos comentários: ')
        print(f'\n{self.nome} {self.sobrenome}\n{self.comentario}')

    def adiciona_amigos(self, amigos:str):
        self.amigos = amigos

    def exibe_amigos(self):
        print('\nConexões: ')
        print(f'{self.amigos}')
