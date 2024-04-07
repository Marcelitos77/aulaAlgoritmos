valorSalario = float(input("Digite o valor do salário: "))

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

if valorSalario <= 1500:
    valorComAcrescimo = valorSalario * 1.2
    print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")
elif valorSalario > 1500 or valorSalario <= 2500:
    valorComAcrescimo = valorSalario * 1.1
    print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")
else:
    valorComAcrescimo = valorSalario * 1.05
    print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")
