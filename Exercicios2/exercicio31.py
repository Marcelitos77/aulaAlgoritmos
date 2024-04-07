import math


valor = int(input("Digite um valor inteiro: "))

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")


if valor == 1 or valor <=3:
    resultado = valor ** 2
    print(f"O valor elevado ao quadrado é: {resultado:.2f}")
elif valor == 4 or valor <= 5:
    resultado = valor ** 0.5  
    print(f"A raiz quadrada do valor é: {resultado:.2f}")
elif valor == 6 or valor <= 9:
    resultado = valor / 9
    print(f"O valor dividido por 9 é: {resultado:.2f}")
else:
    print("Valor fora das condições especificadas.")
