import random
import os
from pathlib import Path
from random import randrange
from random import choices


def allMatches():
    print("Calculadora liga Futebol v2.1 by gwag")
    print("Agradecimento especial ao Resina1 e a Vila Chã de Sá")
    print("50-0 Never forget")
    print("Copyright 2005-2024 gwag Ltd.")
    print("")
    print("")
    lst = []                #lista das equipas
    jogos = []              #lista dos jogos
    resultados = {}         #dict com resultado de cada jogo
    tabela = {}             #Vitorias, empates, derrotas, GM, GS, pontos
    liga = str(input("Introduza o nome da Liga: "))
    while True:
        equipa = input("Introduza a equipa (prima N quando estiver feito): ")
        equipa = equipa.rstrip()
        if equipa == "n" or equipa == "N":
            if len(lst)<2:
                print("Introduz pelo menos 2 equipas")
                continue
            else:
                break
        elif equipa == "":
            print("Introduz um nome válido")
            continue
        else:
            lst.append(equipa)
            continue

    n = 0
    for casa in lst:
        for fora in lst:
            if casa != fora:
                jogos.append((casa,fora))
                n += 1
    
    for y in jogos:
        x = y
        y = jogos.index(y)
        while True:
            resultado1 = choices([0,1,2,3,4,5,6,7,8,9,10], [0.32,0.21,0.187,0.14,0.06,0.03,0.02,0.015,0.01,0.005,0.003])[0]
            resultado2 = choices([0,1,2,3,4,5,6,7,8,9,10], [0.32,0.21,0.187,0.14,0.06,0.03,0.02,0.015,0.01,0.005,0.003])[0]
            resultados[x] = str(resultado1) + "-" + str(resultado2)

            break
        while True:
            if x[0] in tabela:
                if int(resultado1) > int(resultado2):
                    tabela[x[0]][0] += 1 
                    tabela[x[0]][5] += 3
                elif int(resultado1) == int(resultado2):
                    tabela[x[0]][1] += 1
                    tabela[x[0]][5] += 1
                elif int(resultado1) < int(resultado2):
                    tabela[x[0]][2] += 1 
                tabela[x[0]][3] += int(resultado1)
                tabela[x[0]][4] += int(resultado2)
                break
            else:
                tabela[x[0]] = [0,0,0, 0,0, 0]
                continue

        while True:
            if x[1] in tabela:
                if int(resultado1) > int(resultado2):
                    tabela[x[1]][2] += 1 
                elif int(resultado1) == int(resultado2):
                    tabela[x[1]][1] += 1
                    tabela[x[1]][5] += 1
                elif int(resultado1) < int(resultado2):
                    tabela[x[1]][0] += 1
                    tabela[x[1]][5] += 3
                tabela[x[1]][4] += int(resultado1)
                tabela[x[1]][3] += int(resultado2)
                break
            else:
                tabela[x[1]] = [0,0,0, 0,0, 0]
                continue
        
    tabela = dict(sorted(tabela.items(), key=lambda item: (item[1][5],int(item[1][3])-int(item[1][4])),reverse=True,))

    print("Número de jogos: " + str(n))
    print("Equipas: " + str(', '.join(lst)))
    #print(jogos)
    #print(tabela)
    print("Resultado dos jogos" + str(resultados))
    print('-'*210, '\n| {:^206} |'.format(liga))
    print('-'*210, '\n| {:^80} | {:<20} | {:<20} | {:<20} | {:<20} | {:<20} | {:<8} |'.format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos sofridos", "Pontos",))
    print('-'*210)
    for x in tabela:
        print('| {:^80} | {:<20} | {:<20} | {:<20} | {:<20} | {:<20} | {:<8} |'.format(x, tabela[x][0],tabela[x][1],tabela[x][2],tabela[x][3],tabela[x][4],tabela[x][5],))
    
    print('-'*210, "\n \n {:^206}" .format("Parabéns ao " + str(list(tabela)[0] + " por vencer a " + liga + "!")))


    Path("Futebol League Python/Resultados").mkdir(parents=True, exist_ok=True)

    liga2 = liga.replace(" ", "_")

    with open("Futebol League Python/Resultados/" + liga2 + ".txt", "w",encoding='utf-8') as f:
        f.write("Número de jogos: " + str(n) + "\n")
        f.write("Equipas: " + str(', '.join(lst)) + "\n")
        f.write('-'*210 + "\n")
        f.write('| {:^206} |\n'.format(liga))
        f.write('-'*210 + "\n")
        f.write('| {:^80} | {:<20} | {:<20} | {:<20} | {:<20} | {:<20} | {:<8} |\n'.format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos sofridos", "Pontos",))
        f.write('-'*210 + "\n")
        for x in tabela:
            f.write('| {:^80} | {:<20} | {:<20} | {:<20} | {:<20} | {:<20} | {:<8} |\n'.format(x, tabela[x][0],tabela[x][1],tabela[x][2],tabela[x][3],tabela[x][4],tabela[x][5],))
        f.write('-'*210 + "\n")
        f.write("\n \n {:^206}\n" .format("Parabéns ao " + str(list(tabela)[0] + " por vencer a " + liga + "!")))
    
if __name__ == "__main__":
    allMatches()