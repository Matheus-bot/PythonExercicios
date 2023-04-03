# 83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está  com os parêntesess abertos e fechados na ordem correta.

expr = str(input('Digite a espressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está válida! ')
else:
    print('A expressão está errada! ')