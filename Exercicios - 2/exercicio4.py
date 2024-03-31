genero = input("Digite o seu sexo (feminino F, masculino M): ")
altura = float(input("Digite a sua altura em metros: "))

if genero.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:  
    peso_ideal = (72.7 * altura) - 58

nome = "Marcelo Siqueira Oliveira"
ra = "105139241006"
turma = "Desenvolvimento de Software Multiplataforma"

print("\n")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
print(f"Seu peso ideal é {peso_ideal:.2f} kg.")

