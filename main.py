# interajam aqui
import random
lista_nomes = ["icaro", "moy",  "rafael", "kohei"]
while True:
    nome  = random.choice(lista_nomes)
    print(f"o escolhido do time é {nome}")
    resposta = ' '
    while resposta not in "simnao":
        resposta =  input("deseja continuar?[sim/nao]: ").strip().lower()
        if resposta in "simnao":
            break
    if resposta in "nao":
        break 