#Esse programa coleta e exibe o retorno da pesquisa de atendimento ao cliente 
#Autor: Luan-S-Marin

import os

os.system("cls")


#Inicio 

print("========== TudoWeb ==========")
print("==== Pesquisa de opinião ====")

#Definição da quantidade de cada avaliação antes do começo do programa
quant_excelente = 0
quant_bom = 0
quant_ruim = 0

#Entrada de dados e contador de avaliações  
for i in range (1,51):
  nome_usuario = input("Digite o seu nome: ")
  idade_usuario = int(input("Digite a sua idade: "))
  op_usuario = input("Como avalia a sua experiencia na TudoWeb? Escolha entre Excelente(1)/Bom(2)/Ruim(3): ")
  if op_usuario == "1":
    quant_excelente += 1
  elif op_usuario == "2":
    quant_bom += 1
  elif op_usuario == "3":
    quant_ruim += 1


#saida de dados e exibição da quandidade das avaliações "excelente", "bom" e "ruim"

print("Obrigado por participar da pesquisa!")
print("Quantidade de avaliaçoes:")
print(f"Excelente: {quant_excelente}")
print(f"Bom: {quant_bom}")
print(f"Ruim: {quant_ruim}")
