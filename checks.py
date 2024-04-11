import dados
import random
import inimigos
from ataque import calcularAtaque
from player import Player

def resist():
    inimigo = inimigos.inimigoAleatorio()
    resistencia = inimigo["resistencia"]
    if inimigo["tipo"] == "Soldado":
        tipoInimigo = "Soldado"
    elif inimigo["tipo"] == "Monstro":
        tipoInimigo = "Monstro"
    elif inimigo["tipo"] == "Demônio":
        tipoInimigo = "Demônio"
    else:
        tipoInimigo = "Desconhecido"
    print("Você está enfrentando um: ", tipoInimigo)
    print("A resistênia do inimigo é: ", resistencia)
    return resistencia

def ataque():
    global hp_inimigo
    player = Player()
    enemy = inimigos.inimigoAleatorio()
    hp_inimigo = enemy["hp"]
    resistencia = resist()
    resistido = False

    while hp_inimigo > 0:
        atacar = input("Deseja atacar?\n S/Y - Sim/Yes\n N - Não/No\n").upper()
        if atacar == "N":
            print("Você vai tentar fugir, um dado será rolado!")
            dadoFuga = random.randint(1, 20)
            print("O dado da fuga foi:", dadoFuga)
            if dadoFuga > resistencia:
                print("Parabéns, você fugiu!")
            else:
                print("Você terá que lutar!")
                quantidadeDados = int(input("Quantos dados deseja rodar?\nDigite a quantidade entre 1 e 10: "))
                somaDados = dados.rollDice(quantidadeDados)
                print("A soma dos dados é:", somaDados)
                #calculando ataque
    
                forcaAtaque = calcularAtaque(player.strength,quantidadeDados)
    
                if forcaAtaque >= resistencia:
                    dano = forcaAtaque - resistencia
                    print("Você causou ",dano," de dano no inimigo!")
                    
                    #cheque de resistência
                    if not resistido:
                        print("A resistência dele foi quebrada!")
                        danoExtra = dano // 2
                        hp_inimigo -= danoExtra
                        print("Você causou: ",danoExtra," de dano extra no inimigo!")
                        resistido = True
                    else:
                        print("O inimigo já teve sua resistência quebrada, nenhum dano extra!")
                    
                    #atualizando HP
                    
                    hp_inimigo -= dano
                    
                    if (hp_inimigo <= 0):
                        print("Você derrotou o inimigo!")
                    else:
                        print(f"Ele ainda está de pé e com {hp_inimigo} de HP!")
                else:
                    print("O inimigo resistiu seu ataque!")
    
        elif atacar == "S" or atacar == "Y":  # Corrected condition
            quantidadeDados = int(input("Quantos dados deseja rodar?\nDigite a quantidade entre 1 e 10: "))
            somaDados = dados.rollDice(quantidadeDados)
            print("A soma dos dados é:", somaDados)
            #calculando ataque
            forcaAtaque = calcularAtaque(player.strength,quantidadeDados)
            if forcaAtaque >= resistencia:
                dano = forcaAtaque - resistencia
                print("Você causou ",dano," de dano no inimigo!")

                if not resistido:
                        print("A resistência dele foi quebrada!")
                        danoExtra = dano // 2
                        hp_inimigo -= danoExtra
                        print("Você causou: ",danoExtra," de dano extra no inimigo!")
                        resistido = True
                else:
                    print("O inimigo já teve sua resistência quebrada, nenhum dano extra!")
                    

                #atualizando HP
                hp_inimigo -= dano
                
                if (hp_inimigo <= 0):
                    print("Você derrotou o inimigo!")
                else:
                    print(f"Ele ainda está de pé e com {hp_inimigo} de HP!")
            else:
                print("O inimigo resistiu seu ataque!")
        else:
            print("Opções inválidas!")

ataque()
