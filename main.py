# interajam aqui
import random
lista_nomes = ["icaro", "moy",  "rafael", "kohei"]
while True:
    nome  = random.choice(lista_nomes)
    print(f"o escolhido do time é {nome}")
    resposta = ' '
    while resposta not in "sn" or resposta == "nao" or resposta =="sim":
        resposta =  input("deseja continuar?[sim/nao]: ").strip().lower()
        if resposta in "sn" or resposta == "nao" or resposta =="sim":
            break
        else:
            print("escreva uma escolha valida")
    if resposta in "n" or resposta == "nao":
        break 