class Calculadora:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def Soma(self):
        return self.a + self.b
    
    def Subtrair(self):
        return self.a - self.b

    def Multiplicar(self):
        return self.a * self.b

    def Dividir(self):
        return self.a / self.b

loop = 'S'
while loop == 'S':
    try:
        a = float(input('\nDigite o 1º valor: '))
        b = float(input('\nDigite o 2º valor: '))
        menu = int(input('''\nEscolha uma das seguintes opções: \n
1: Somar
2: Subtrair
3: Multiplicar
4: Dividir
\nQual a sua opção? '''))
        if menu == 1:
            print(f'\n{a} + {b} = {Calculadora(a, b).Soma():.2f}')
        elif menu == 2:
            print(f'\n{a} - {b} = {Calculadora(a, b).Subtrair():.2f}')
        elif menu == 3:
            print(f'\n{a} x {b} = {Calculadora(a, b).Multiplicar():.2f}')
        elif menu == 4:
            print(f'\n{a} / {b} = {Calculadora(a, b).Dividir():.2f}')
    except ZeroDivisionError:
        print('Erro: não é possível fazer divisão por zero.')
    except ValueError:
        print('Erro: digite um número.')   
    loop = input('\nDeseja continuar? (S/N) ').upper()
print('\nObrigado e volte sempre!')
