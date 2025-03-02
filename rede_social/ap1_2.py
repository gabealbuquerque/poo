from ap1_2_funcoes import *

postagens = []
comentarios = []

nome = 'Gabriel'
sobrenome = 'Vasconcelos'
email = 'eugabrieldealbuquerque@gmail.com'
celular = '11 12345-6789'
data_nascimento = '25/02/2005'
sexo = 'M'

perfil2 = Perfil(nome, sobrenome, email, celular, data_nascimento, sexo)

titulo = 'Il fait trop chaud'
texto = 'Está muito quente'
postagens.append(criar_postagem(titulo, texto))

nome = 'Naiara'
sobrenome = 'Alves'
email = 'alvesnaiara@hotmail.com'
celular = '11 12345-6789'
data_nascimento = '17/04/1997'
sexo = 'F'

perfil3 = Perfil(nome, sobrenome, email, celular, data_nascimento, sexo)

comentarios.append(comentar_postagem('Realmente! Está muito quente.'))

print('_-' * 15, 'REDE SOCIAL ALB', '-_' * 15)

print('\nSeja bem-vindo à Rede Social ALB!')
print('\nA seguir preencha os campos para criar o seu perfil: ')

# Solicitando dados e atribuindo a variáveis
nome = input('\nDigite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
email = input('Digite o seu email: ')
celular = input('Digite o seu número de celular: ')
data_nascimento = input('Digite a sua data de nascimento: ')
sexo = input('Digite o seu sexo: ')

perfil_usuario  = Perfil(nome, sobrenome, email, celular, data_nascimento, sexo)
# Criando variável a qual chama a classe Perfil e passa como parâmetro todos os dados inseridos.

# Chamando a função exibir dados para mostrar ao usuário os dados passados.
print('\nPerfil criado com sucesso!')
perfil_usuario.exibir_dados()

criar_post = input('\nDeseja criar uma postagem? (S/N) ').upper()
while criar_post != 'S' and criar_post != 'N':
    criar_post = input('\nErro: digite apenas S ou N: ').upper()
while criar_post == 'S':
    titulo = input('\nQual será o título da postagem? ')
    texto = input('\nDigite a postagem: ')
    postagens.append(criar_postagem(titulo, texto))
    postagens.exibir_postagem()
    criar_post = input('\nDeseja criar mais uma postagem? (S/N) ').upper()

print('\nPostagens do dia: ')
print(f'\n{perfil2.nome}')
postagens.exibir_postagem()

print('\nComentários: ')
print(f'{perfil3.nome}')
comentarios.exibir_comentario()

comentario = input('Deseja comentar algum post? (S/N) ').upper()
while comentario != 'S' and comentario != 'N':
    comentario = input('Erro: digite S ou N: ').upper()
while comentario == 'S':
    comentarios.append(input('Digite seu comentário: '))
