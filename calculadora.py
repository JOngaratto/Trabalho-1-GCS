import math

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Número negativo não tem raiz quadrada real!"
    return math.sqrt(a)

def main():
    print("Bem-vindo à Calculadora Simples!")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")

    operacao = input("Digite o número da operação: ")

    if operacao == '5':
        a = float(input("Digite o número: "))
        print("Resultado:", raiz_quadrada(a))
    else:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if operacao == '1':
            print("Resultado:", soma(a, b))
        elif operacao == '2':
            print("Resultado:", subtrai(a, b))
        elif operacao == '3':
            print("Resultado:", multiplica(a, b))
        elif operacao == '4':
            print("Resultado:", divide(a, b))
        else:
            print("Operação inválida!")

if __name__ == "__main__":
    main()
