capital=float(input("Insira o valor ivestido: "))
porcentagem=float(input("Insira a taxa de juros em MESES: "))
periodo=int(input("Insira o período em MESES: "))

taxa= porcentagem/100

juros= capital*taxa*periodo

montante=juros+capital
print("O total do rendimento será: ",montante)