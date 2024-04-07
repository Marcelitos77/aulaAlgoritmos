valor = float(input("Digite um valor: "))

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

if valor % 10 == 0:
    print("O valor é divisível por 10")
elif valor % 5 == 0:
    print("O valor é divisível por 5")
elif valor % 2 == 0:
    print("O valor é divisível por 2")
else:
    print("O valor não é divisível")