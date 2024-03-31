venda1 = float(input("Digite o valor da primeira compra: "))
venda2 = float(input("Digite o valor da segunda compra: "))
venda3 = float(input("Digite o valor da terceira compra: "))

totalVendas = venda1 + venda2 + venda3

desconto = 0

if totalVendas > 300:
    desconto = 0.2
elif totalVendas > 200:
    desconto = 0.15
elif totalVendas > 100:
    desconto = 0.10

descontoTotal = desconto * totalVendas
valorFinal = totalVendas - descontoTotal

nome = "Marcelo Siqueira Oliveira"
ra = "105139241006"
turma = "Desenvolvimento de Software Multiplataforma"


print("")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
print (f"O valor total é {totalVendas:.2f} e o valor com o desconto é {valorFinal:.2f}")