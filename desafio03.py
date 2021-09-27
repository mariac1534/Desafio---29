import os

nome = input("Nome do produto: ")
codigo = int(input("Código do produto: "))
quantidade = int(input("Quantidade: "))
preco = int(input("Preço do produto: "))

resp = quantidade * preco;

print("---------Total da compra")
print("-------Nome do produto:",nome)
print("-----Código do produto:",codigo)
print("---Quantidade comprada:",quantidade)
print("------Preço do produto:",preco,"reais")
print("-Valor total da compra:",resp,"reais")

os.system("pause")