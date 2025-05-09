# 1Ajuste a função checar_parênteses da aula anterior para que ela seja capaz
# de verificar colchetes e chaves em expressões.

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def checar_parenteses(expressao):
    s = Stack()
    balanceada = True
    i = 0
    while i < len(expressao) and balanceada:
        simbolo = expressao[i]
        if simbolo == "(":
            s.push(simbolo)
        if simbolo == ")":
            if s.isEmpty():
                balanceada = False
            else:
                s.pop()
        if simbolo == '[' or ']':
            print('Erro: contém colchete')
        if simbolo == '{' or '}':
            print('Erro: contém chaves.')
        i = i + 1
    if balanceada and s.isEmpty():
        return True
    else:
        return False
expressao = 'hola! ['
teste1 = checar_parenteses(expressao)
