operacao = input(f'1. Soma \n'
                 f'2. Subtração\n'
                 f'3  Divisão\n'
                 f'4. Multiplicação\n')

# Tratamento de erros para entrada da operação
try:
    operacao = int(operacao)
except ValueError:
    print('Entrada inválida para a operação.')

x = float(input('Insira o primeiro numero: '))
y = float(input('Insira o segundo numero:'))

if operacao == 1:
    soma = x + y
    print(f'Resultado da soma: {soma}')
elif operacao == 2:
    subtracao = x - y
    print(f'Resultado da subtração: {subtracao}')
elif operacao == 3:
    if y == 0:
       print('Não é possível dividir por zero.')
    else:
      divisao  = x / y
      print(f'Resultado da divisão: {divisao}')
elif operacao == 4:
    multiplicacao = x * y
    print(f'Resultado da multiplicação: {multiplicacao}')
else:
    print('Operação inválida')
