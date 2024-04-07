nome = str(input("Digite seu nome completo: "))
ra = int(input("Digite seu RA: "))
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = float(nota1 + nota2) / 2

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

if media >= 7:
    print(f"A sua média é: {media:.2f} você está aprovado")
else:
    print(f"A sua média é: {media:.2f}, Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.")
