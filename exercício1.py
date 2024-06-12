capital=int(input("Insira o valor do seu capital: "))
porcentagem=float(input("Insira o valor do juros em MESES: "))
periodo=int(input("Insira o período em MESES: "))

taxa= porcentagem/100

juros= capital*taxa*periodo

montante=juros+capital
print("Você terá: ",montante)
