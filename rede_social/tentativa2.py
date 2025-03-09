from tentativa2_func import *

msg = ' REDE SOCIAL '
print('-_' * len(msg) + msg + '-_' * len(msg))

print('\nPara começar é necessário criar seu perfil! \n\nPreencha os campos abaixo para criar seu perfil: ')

user = input('\nUsername: ').lower()
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
data_de_nascimento = input('Data de nascimento: ')
numero_telefone = input('Número de telefone: ')
email = input('Email: ').lower()
sexo = input('Sexo: (M/F) ').upper()

user1 = RedeSocial(user, nome, sobrenome, data_de_nascimento, numero_telefone, email, sexo)

while True:
    ver_perfil = input('\nVer perfil? (S/N) ').upper()
    if ver_perfil == 'S':
        user1.exibe_perfil()

    print('\nComece uma publicação!')
    criar_post = input('\nCriar publicação? (S/N) ').upper()
    if criar_post == 'S':
        post = input('\nSobre o que você quer falar? ')
        user1.criar_postagem(post)
    ver_post = input('\nVer postagem criada? (S/N) ').upper()
    if ver_post == 'S':
        user1.exibe_postagem()

    print('\nFaça um comentário! ')
    criar_comentario = input('\nCriar comentário? (S/N) ').upper()
    if criar_comentario == 'S':
        comentario = input('\nO que você quer comentar? ')
        user1.criar_comentario(comentario)
    print('\nVeja os comentários! ')
    ver_comentario = input('\nVer comentários? (S/N) ').upper()
    if ver_comentario == 'S':
        user1.exibe_postagem()
        user1.exibe_cometario()

    print('\nAmplie sua rede: ')
    amplicar_rede = input('\nDeseja adicionar amigos? (S/N) ').upper()
    if amplicar_rede == 'S':
        amigos = input('Pesquisar: ')
        user1.adiciona_amigos(amigos)
    print('\nVeja suas conexões!')
    ver_amigos = input('\nDeseja ver suas conexões? (S/N) ').upper()
    if ver_amigos == 'S':
        user1.exibe_amigos()

    sair = input('\nDeseja sair? (S/N) ').upper()
    if sair == 'S':
        break

msg = ' SAINDO '
print('-_' * len(msg) + msg + '-_' * len(msg))