num1 = int(input("Entre com o primeiro número "))
num2 = int(input("Entre com o segundo número: "))

op = input("Qual operação matemática será realizada? ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 != 0:
        print(num1 / num2)
else:
    print("Operação inválida")
        