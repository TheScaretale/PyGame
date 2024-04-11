from player import Player
from dados import rollDice

def calcularAtaque(strength,quantidadeDados):
    jogador = Player()
    attack = jogador.attack()
    ataqueFinal = (attack + strength)+ rollDice(quantidadeDados)
    return ataqueFinal
