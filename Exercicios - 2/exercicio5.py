import math

def calcular_quantidade_tinta(area):
    return area / 6

def calcular_quantidade_tinta_folga(area):
    return area / 6 * 1.1  

def calcular_preco_latas(area):
    quantidade_latas = math.ceil(calcular_quantidade_tinta(area) / 18)
    preco_total = quantidade_latas * 80
    return quantidade_latas, preco_total

def calcular_preco_galoes(area):
    quantidade_galoes = math.ceil(calcular_quantidade_tinta(area) / 3.6)
    preco_total = quantidade_galoes * 35
    return quantidade_galoes, preco_total

def calcular_preco_misto(area):
    quantidade_latas = math.floor(calcular_quantidade_tinta_folga(area) / 18)
    resto = calcular_quantidade_tinta_folga(area) - quantidade_latas * 18
    quantidade_galoes = math.ceil(resto / 3.6)
   
    preco_total = quantidade_latas * 80 + quantidade_galoes * 35
    return quantidade_latas, quantidade_galoes, preco_total

while True:
    try:
        area_a_ser_pintada = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
        break
    except ValueError:
        print("Por favor, digite um valor válido.")

latas, preco_latas = calcular_preco_latas(area_a_ser_pintada)
galoes, preco_galoes = calcular_preco_galoes(area_a_ser_pintada)
latas_misto, galoes_misto, preco_misto = calcular_preco_misto(area_a_ser_pintada)

nome = "Marcelo Siqueira Oliveira"
ra = "105139241006"
turma = "Desenvolvimento de Software Multiplataforma"

print("\n")
print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
print(f"a) Comprar apenas latas de 18 litros: {latas} latas, preço total R$ {preco_latas:.2f}")
print(f"b) Comprar apenas galões de 3,6 litros: {galoes} galões, preço total R$ {preco_galoes:.2f}")
print(f"c) Misturar latas e galões: {latas_misto} latas e {galoes_misto} galões, preço total R$ {preco_misto:.2f}")

