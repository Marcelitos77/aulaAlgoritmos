valor = int(input("digite um valor: "))

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

if valor < 0:
    valorPositivo = abs(valor)
    print(f"O valor é {valorPositivo}")
elif valor > 10:
  novoValor = int(input(f"Valor invalido, digite novo valor: "))
  valorfinal = valor - novoValor
  print(f"A diferença entre os valores é {valorfinal}")
else:
    valorDividido = valor / 5
    print(f"o valor dividido é {valorDividido}")
