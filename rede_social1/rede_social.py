from funcoes_rede_social import *
from verificacoes import *

msg = ' REDE SOCIAL '
print('-_' * len(msg) + msg + '-_' * len(msg))

print('\nPara começar é necessário criar seu perfil! \n\nPreencha os campos abaixo para criar seu perfil: ')

user = input('\nUsername: ').lower()
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
data_de_nascimento = input('Data de nascimento: ')
data_verifica = verifica_data(data_de_nascimento)
data_de_nascimento = data_verifica
numero_telefone = input('Número de telefone: ')
numero_verifica = verifica_telefone(numero_telefone)
numero_telefone = numero_verifica
email = input('Email: ').lower()
email_verifica = verifica_email(email)
email = email_verifica
sexo = input('Sexo: (M/F) ').upper()
sexo_verifica = verifica_sexo(sexo)
sexo = sexo_verifica

user1 = RedeSocial(user, nome, sobrenome, data_de_nascimento, numero_telefone, email, sexo)

ver_perfil = input('\nVer perfil? (S/N) ').upper()
ver_perfil_verifica = verifica_opcao_ver_perfil(ver_perfil)
ver_perfil = ver_perfil_verifica
if ver_perfil == 'S':
    user1.exibe_perfil()
    
while True:
    print('\nComece uma publicação!')
    criar_post = input('\nCriar publicação? (S/N) ').upper()
    criar_post_verifica = verifica_opcao_criar_post(criar_post)
    criar_post = criar_post_verifica
    if criar_post == 'S':
        post = input('\nSobre o que você quer falar? ')
        user1.criar_postagem(post)
    ver_post = input('\nVer postagem criada? (S/N) ').upper()
    ver_post_verifica = verifica_opcao_ver_post(ver_post)
    ver_post = ver_post_verifica
    if ver_post == 'S':
        user1.exibe_postagem()

    print('\nFaça um comentário! ')
    criar_comentario = input('\nCriar comentário? (S/N) ').upper()
    criar_comentario_verifica = verifica_opcao_criar_comentario(criar_comentario)
    criar_comentario = criar_comentario_verifica
    if criar_comentario == 'S':
        comentario = input('\nO que você quer comentar? ')
        user1.criar_comentario(comentario)
    print('\nVeja os comentários! ')
    ver_comentario = input('\nVer comentários? (S/N) ').upper()
    ver_comentario_verifica = verifica_opcao_ver_comentario(ver_comentario)
    if ver_comentario == 'S':
        user1.exibe_postagem()
        user1.exibe_cometario()

    print('\nAmplie sua rede: ')
    ampliar_rede = input('\nDeseja adicionar amigos? (S/N) ').upper()
    ampliar_rede_verifica = verifica_opcao_ampliar_rede(ampliar_rede)
    ampliar_rede = ampliar_rede_verifica
    if ampliar_rede == 'S':
        amigos = input('Pesquisar: ')
        user1.adiciona_amigos(amigos)
    print('\nVeja suas conexões!')
    ver_amigos = input('\nDeseja ver suas conexões? (S/N) ').upper()
    ver_amigos_verifica = verifica_opcao_ver_amigos(ver_amigos)
    ver_amigos = ver_amigos_verifica
    if ver_amigos == 'S':
        user1.exibe_amigos()

    sair = input('\nDeseja sair? (S/N) ').upper()
    sair_verifica = verifica_opcao_sair(sair)
    sair = sair_verifica
    if sair == 'S':
        break

msg = ' SAINDO '
print('-_' * len(msg) + msg + '-_' * len(msg))
