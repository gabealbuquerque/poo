from ap1_2_funcoes import *
print('_-' * 15, 'REDE SOCIAL ALB', '-_' * 15)

print('\nSeja bem-vindo à Rede Social ALB. A seguir preencha os campos para criar o seu perfil: ')

nome = input('\nDigite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
email = input('Digite o seu email: ')
celular = input('Digite o seu número de celular: ')
data_nascimento = input('Digite a sua data de nascimento: ')
sexo = input('Digite o seu sexo: ').upper

perfil1 = RedeSocial(nome, sobrenome, email, celular, data_nascimento, sexo)

print('\nSeu perfil foi criado com os seguintes dados: ')
print(f'\nNome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Email: {email}')
print(f'Celular: {celular}')
print(f'Data de Nascimento: {data_nascimento}')
print(f'Sexo: {sexo}')

