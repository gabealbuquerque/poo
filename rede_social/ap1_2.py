import datetime
from ap1_2_funcoes import *

print('\nBem vindo! Para começar, é necessário criar seu perfil.')
print('\nPreencha os campos a seguir para criar seu perfil: ')

# Perfis fictícios
nome = 'Gabriel'
sobrenome = 'Vasconcelos'
data_nascimento = '25/02/2005'
email = 'gabe@gmail.com'
celular = '11 12345-6789'
sexo = 'M'

perfilGabriel = Perfil(nome, sobrenome, data_nascimento, email, celular, sexo)

nome = 'Rodnald'
sobrenome = 'Demitroff'
data_nascimento = '11/02/1998'
email = 'assis@gmail.com'
celular = '11 12345-6789'
sexo = 'M'

perfilRodnald = Perfil(nome, sobrenome, data_nascimento, email, celular, sexo)

# Solicita dados para criação do perfil
nome = input('\nDigite seu 1º nome: ')
sobrenome = input('Digite seu sobrenome: ')
data_nascimento = input('Digite sua data de nascimento: ')
email = input('Digite seu email: ')
celular = input('Digite seu número de telefone: ')
sexo = input('Digite o seu sexo: (M/F) ').upper()

#atribui uma variavel para a chamada da classe Perfil e passa os dados como parâmetro
perfil1 = Perfil(nome, sobrenome, data_nascimento, email, celular, sexo)
#através da variável da chamada da classe, chama a função exibe perfil para exibir os dados das classes
perfil1.exibePerfil()

# Postagens

print(f'\nPOSTAGENS DO DIA ({datetime.date.today()}): ')

postagemGabriel = "J'adore escouter les musiques d'Alejandro Lema"
postagemGabriel1 = Postagem(postagemGabriel)
print(f'\n{perfilGabriel.nome}')
postagemGabriel1.exibePostagem()

postagemRodnald = "Il fait trop chaud en cette week-end!"
postagemRodnald1 = Postagem(postagemRodnald)
print(f'\n{perfilRodnald.nome}')
postagemRodnald1.exibePostagem()
postagemRodnald1.exibeComentario()

# Comentarios
comentarioGabriel = "Je detéste le chaud! "
postagemRodnald1.adicionaComentario(comentarioGabriel)


#solicita o compartilhamento de ideia (criação do post)
post1 = input('\nCompartilhe suas ideias... ')
#chama a classe através de uma variável 
postagem1 = Postagem(post1)
#exibe o nome do criador da postagem
print(f'\n{perfil1.nome} {perfil1.sobrenome}')
#exibe a postagem
postagem1.exibePostagem()


#solicita um comentário
comentario = input('\nAdicionar comentário... ')
#atribui comentario a classe postagem
postagem1.adicionaComentario(comentario)

#exibe o perfil do dono do comentário
print('\nComentários: ')
print(f'\n{perfil1.nome}')
postagem1.exibeComentario()
