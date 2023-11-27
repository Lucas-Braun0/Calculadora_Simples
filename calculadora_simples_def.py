def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    if y == 0:
        print('Não divide por ZERO')
        return None
    return x / y

def multiplicacao(x, y):
    return x * y

operacao = input(f'1. Soma \n'
                 f'2. Subtração\n'
                 f'3. Divisão\n'
                 f'4. Multiplicação\n')

# Tratamento de erros para entrada da operação
try:
    operacao = int(operacao)
except ValueError:
    print('Entrada inválida para a operação.')
    exit(1)

x = float(input('Insira o primeiro número: '))
y = float(input('Insira o segundo número: '))

if operacao == 1:
    resultado = soma(x, y)
    print(f'Resultado da soma: {resultado}')
elif operacao == 2:
    resultado = subtracao(x, y)
    print(f'Resultado da subtração: {resultado}')
elif operacao == 3:
    resultado = divisao(x, y)
    if resultado is not None:
        print(f'Resultado da divisão: {resultado}')
elif operacao == 4:
    resultado = multiplicacao(x, y)
    print(f'Resultado da multiplicação: {resultado}')
else:
    print('Operação inválida')
