print(f"Digite o número da operação desejada:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potenciação")
operacao = int(input(""))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == 1:
    resultado = num1 + num2

elif operacao == 2:
    resultado = num1 - num2

elif operacao == 3:
    resultado = num1 * num2

elif operacao == 4:
    resultado = num1 / num2

elif operacao == 5: 
    resultado = num1 ** num2

print(f"O resultado da operação é {resultado}")
