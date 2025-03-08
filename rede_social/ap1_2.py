from ap1_2_funcoes import *

nome = input('\nDigite seu 1º nome: ')
sobrenome = input('Digite seu sobrenome: ')
data_nascimento = input('Digite sua data de nascimento: ')
email = input('Digite seu email: ')
celular = input('Digite seu número de telefone: ')
sexo = input('Digite o seu sexo: (M/F) ').upper()

perfil1 = Perfil(nome, sobrenome, data_nascimento, email, celular, sexo)
perfil1.exibePerfil()

post1 = input('\nCompartilhe suas ideias... ')
postagem1 = Postagem()
postagem1.exibePostagem(post1)

