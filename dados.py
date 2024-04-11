import random

def rollDice(quantDados):
    somaTotal = 0

    facesPossiveis = [1,2,3,4,5,6]
    for dado in range(quantDados):
        roll = random.choice(facesPossiveis)
        somaTotal += roll
    return(somaTotal)