def verifica_data(data_nascimento):
    while len(data_nascimento) != 10:
        data_nascimento = input('Erro: certifique que a data tenha 8 dígitos e 2 barras: ')
    while '/' not in data_nascimento:
        data_nascimento = input('Erro: certifique que a data tenha o padrão do exemplo: ')
        if '/' in data_nascimento:
            break
    return data_nascimento

def verifica_telefone(numero_telefone):
    while '-' not in numero_telefone:
        numero_telefone = input('Erro: certifique que o numero de telefone tenha hífen (-): ')
        if '-' in numero_telefone:
            break
    return numero_telefone
    
def verifica_email(email):
    while '@' not in email:
        email = input('Erro: certifique que o email tenha "@": ')
        if '@' in email:
            break
    return email

def verifica_sexo(sexo):
    while sexo != 'M' and sexo != 'F':
        sexo = input('Erro: digite M ou F: ').upper()
    return sexo

def verifica_opcao_ver_perfil(ver_perfil):
    while ver_perfil != 'S' and ver_perfil != 'N':
        ver_perfil = input('Erro: digite apenas S ou N: ').upper()
    return ver_perfil

def verifica_opcao_criar_post(criar_post):
    while criar_post != 'S' and criar_post != 'N':
        criar_post = input('Erro: digite apenas S ou N: ').upper()
    return criar_post

def verifica_opcao_ver_post(ver_post):
    while ver_post != 'S' and ver_post != 'N':
        ver_post = input('Erro: digite apenas S ou N: ').upper()
    return ver_post

def verifica_opcao_criar_comentario(criar_comentario):
    while criar_comentario != 'S' and criar_comentario != 'N':
        criar_comentario = input('Erro: digite apenas S ou N: ').upper()
    return criar_comentario

def verifica_opcao_ver_comentario(ver_comentario):
    while ver_comentario != 'S' and ver_comentario != 'N':
        ver_comentario = input('Erro: digite apenas S ou N: ').upper()
    return ver_comentario

def verifica_opcao_ampliar_rede(ampliar_rede):
    while ampliar_rede != 'S' and ampliar_rede != 'N':
        ampliar_rede = input('Erro: digite apenas S ou N: ').upper()
    return ampliar_rede

def verifica_opcao_ver_amigos(ver_amigos):
    while ver_amigos != 'S' and ver_amigos != 'N':
        ver_amigos = input('Erro: digite apenas S ou N: ').upper()
    return ver_amigos

def verifica_opcao_sair(sair):
    while sair != 'S' and sair != 'N':
        sair = input('Erro: digite apenas S ou N: ').upper()
    return sair