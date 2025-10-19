# calculadora simples

num1 = 0
num2 = 0
resultado = 0
op = ''

while True:

    num1 = float(input('Digite o primeiro número'))

    op = input('Digite a opreção matemática')
    num2 = float(input('digite o segundo numero:'))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op =='/':
        result = num1 / num2
    elif op == '*':
        result = num1 * num2
    else:
        print('você digitou icorretamente')
    print('{} {} {} = {}'.format(num2, op, num2, result))