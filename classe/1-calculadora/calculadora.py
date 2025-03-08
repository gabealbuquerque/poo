from classes import *

menu = int(input('''\nEscolha uma das opções abaixo:\n
1: Comprimento / Tempo / Velocidade / Área
2: Massa / IMC
3: Temperatura / Líquido
4: Moeda / Calculadora
5: Nota simples / Tabuada
\nQual a sua opção? '''))

if menu == 1:
    menu1 = int(input('''\nDigite uma das opções abaixo: \n
1: Comprimento
2: Tempo
3: Velocidade
4: Área 
\nQual a sua opção? '''))
    if menu1 == 1:
        metros = float(input('\nDigite quantos metros você gostaria de converter para centímetros: (m) '))
        Comprimento(menu1, metros)
        

elif menu == 4:
    menu4 = int(input('''\nDigite uma das opções abaixo: \n
1: Moeda
2: Calculadora
\nQual a sua opção? '''))
    if menu4 == 2:
        num1 = float(input('\nDigite o primeiro número: '))
        num2 = float(input('\nDigite o segundo número: '))
        opcao = int(input('''\nEscolha uma das opções abaixo:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão 
        \nQual a sua opção? '''))
        Calculadora(opcao, num1, num2)
