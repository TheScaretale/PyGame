import random

def soldado():
    return {"tipo": "Soldado",  "hp": 50, "resistencia": random.randint(1, 20)}

def monstro():
    return {"tipo": "Monstro", "hp": 80, "resistencia": random.randint(1, 20)}

def demonio():
    return {"tipo": "Demônio", "hp": 150, "resistencia": random.randint(1, 20)}

def inimigoAleatorio():
    probabilidade=[0.6,0.3,0.1]
    inimigos = [soldado,monstro,demonio]


    inimigoSelecionado = random.choices(inimigos, weights=probabilidade)[0]
    return inimigoSelecionado()
