capital=float(input("Insira o valor investido: "))
porcentagem=float(input("Insira a taxa de juros em MESES: "))
periodo=int(input("Insira o período em MESES: "))

taxa= porcentagem/100

montante=capital*(1+taxa)**periodo
print("O total do seu investimento será: ", montante)