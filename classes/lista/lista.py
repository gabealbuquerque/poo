class Lista:
    def __init__(self, lista:list):
        self.lista = list
    
lista = [] 

while len(lista) <= 10:
    print(f'\nLista atual: {lista} - Tam: {len(lista)}.')
    try: 
        num = int(input('\nDigite um valor para preencher a lista ou -1 para parar: '))
        if num == -1:
            break
        lista.append(num)
    except ValueError:
        print('Erro: digite um número inteiro.')
    except IndexError as e:
        print(f'Erro: a lista tem mais de 10 valores! {e}')
    print('\nVolte sempre!')
