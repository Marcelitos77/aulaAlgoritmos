valorDaCompra = float(input("Digite o valor da compra: "))

nome = "Marcelo Siqueira Oliveira"
ra = "105139241006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

if valorDaCompra >= 300:
    valorComdesconto = valorDaCompra * 0.8
    print(f"O valor a ser pago com desconto é R$ {valorComdesconto:.2f}")
elif valor == 200 or valor < 300:
    valorComdesconto = valorDaCompra * 0.90
    print(f"O valor a ser pago com desconto é R$ {valorComdesconto:.2f}")
else:
    valorComdesconto = valorDaCompra * 0.95
    print(f"O valor a ser pago com desconto é R$ {valorComdesconto:.2f}")

