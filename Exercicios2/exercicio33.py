nome = str(input("Digite seu nome completo: "))
ra = int(input("Digite seu RA: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")


if media >= 7:
    print(f"Sua média é: {media:.2f}. Você está aprovado.")
else:
    print(f"Sua média é: {media:.2f}. Você ainda tem uma chance! Estude mais para o exame.")
    exame = float(input("Digite a nota do exame: "))
    notaFinal = (media + exame) / 2

    
    if notaFinal >= 5:
        print("Parabéns, você aproveitou a sua chance! Está aprovado.")
    else:
        print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")
