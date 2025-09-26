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

def potencia(a, b):
    return a ** b

def main():
    print("Bem-vindo à Calculadora Simples!")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")

    operacao = input("Digite o número da operação: ")
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
    elif operacao == '5':
        print("Resultado:", potencia(a, b))
    else:
        print("Operação inválida!")

if __name__ == "__main__":
    main()
