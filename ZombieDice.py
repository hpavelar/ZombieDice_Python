'''ALUNO: Henrique Pereira de Avelar
CURSO: Análise e Desenvolvimento de sistemas'''


#importando bibliotecas e funções:
import random
import time


#listas globais:
players = []
dados_sorteados = []
faces_sorteadas = []
jogador = [0, 0, 0]
pontuacoes = []


#variáveis globais:
player = 0
tiros = 0
cerebros = 0
passos = 0


#coletando o número de jogadores e o nome de cada um deles e adicionando à lista players:
n_players = int(input("Quantos zumbis vão jogar? "))
if n_players < 2:
    print("\nVOCÊ NÃO PODE JOGAR SOZINHO!\nProcure um amigo.")
else:
    for player in range(n_players):
        nome = input("Qual é o seu nome, zumbi {}? ".format(player+1))
        players.append(nome)
    

    #adicionando uma entrada com valor 0 na lista pontuacoes para cada jogador
    for i in range(n_players):
        pontuacoes.append(0) 


    #função que cria os dados como tuplas e os adicionando na lista dados:
    def copo(dados):
        d_verde = ("C", "C", "C", "P", "P", "T")
        d_amarelo = ("C", "C", "P", "P", "T", "T")
        d_vermelho = ("C", "P", "P", "T", "T", "T")
        for i in range(6):
            dados.append(d_verde)
        for i in range(4):
            dados.append(d_amarelo)
        for i in range(3):
            dados.append(d_vermelho)
        return dados
    #inicializando a lista dados vazia e adicionando os dados pela função copos:
    dados = []
    dados = copo(dados)


    #função que sorteia 3 dados e os adiciona à lista dados_sorteados:
    def sortear_dados():
        d1 = random.choice(dados)
        dados.remove(d1)
        dados_sorteados.append(d1)
        d2 = random.choice(dados)
        dados.remove(d2)
        dados_sorteados.append(d2)
        d3 = random.choice(dados)
        dados.remove(d3)
        dados_sorteados.append(d3)
        print("DADOS SORTEADOS:")
        if d1 == ("C", "C", "C", "P", "P", "T"):
            print("\033[0;49;32mDado verde.\033[m")
        elif d1 == ("C", "C", "P", "P", "T", "T"):
            print("\033[0;49;33mDado amarelo.\033[m")
        elif d1 == ("C", "P", "P", "T", "T", "T"):
            print("\033[0;49;91mDado vermelho.\033[m")
        if d2 == ("C", "C", "C", "P", "P", "T"):
            print("\033[0;49;32mDado verde.\033[m")
        elif d2 == ("C", "C", "P", "P", "T", "T"):
            print("\033[0;49;33mDado amarelo.\033[m")
        elif d2 == ("C", "P", "P", "T", "T", "T"):
            print("\033[0;49;91mDado vermelho.\033[m")
        if d3 == ("C", "C", "C", "P", "P", "T"):
            print("\033[0;49;32mDado verde.\033[m")
        elif d3 == ("C", "C", "P", "P", "T", "T"):
            print("\033[0;49;33mDado amarelo.\033[m")
        elif d3 == ("C", "P", "P", "T", "T", "T"):
            print("\033[0;49;91mDado vermelho.\033[m")

    
    #função que sorteia 1 face de cada dado da lista dados_sorteados:
    def sortear_faces():
        f1 = random.choice(dados_sorteados[0])
        f2 = random.choice(dados_sorteados[1])
        f3 = random.choice(dados_sorteados[2])
        faces_sorteadas.append(f1)
        faces_sorteadas.append(f2)
        faces_sorteadas.append(f3)
        print("\nFACES SORTEADAS:\n{}, {}, {}.".format(f1, f2, f3))
        if f1 == "C":
            jogador[0] += 1
        if f1 == "T":
            jogador[1] += 1
        if f1 == "P":
            jogador[2] += 1
        if f2 == "C":
            jogador[0] += 1
        if f2 == "T":
            jogador[1] += 1
        if f2 == "P":
            jogador[2] += 1
        if f3 == "C":
            jogador[0] += 1
        if f3 == "T":
            jogador[1] += 1
        if f3 == "P":
            jogador[2] += 1
            
        
    #função que verifica se um jogador venceuo jogo:
    def vencedor():
        if pontuacoes[player] >= 13:
            print("\033[0;101;36m\n------------------------------------------------------------------------------------------\nESPERE AÍ, {}!!!\nVOCÊ VENCEU!!!!\n------------------------------------------------------------------------------------------\033[m".format(players[player].upper()))
            

    #execução do jogo:
    while True:
        print("\n------------------------------------------------------------------------------------------\n-É SUA VEZ, {}!-".format(players[player].upper()))
        sortear_dados()
        sortear_faces()
        #se o jogador tomou 3 ou mais tiros, não soma pontos na rodada e passa a vez
        if jogador[1] >= 3:
            print("\033[0;49;91mQue pena, você tomou 3 tiros e vai ter que passar a vez :/\033[m")
            pontuacoes[player] += 0
            #exibindo a pontuação de cada jogador até o momento:
            print("\n===PONTUAÇÃO ATUAL:===")
            for i in range(len(players)):
                print("{}: {}".format(players[i], pontuacoes[i]))
            time.sleep(1.5)
            vencedor()
            player += 1
            #reiniciando as listas dados, dados sorteados, faces e jogador:
            dados = []
            dados = copo(dados)
            dados_sorteados = []
            faces_sorteadas = []
            jogador = [0, 0, 0]
            if player == len(players):
                player = 0
                continue 
            continue
        #se o jogador não tomou 3 tiros, deve escolher entre jogar novamente ou não. 
        else:
            print("------------------------------------------------------------------------------------------")
            print("Cérebros comidos: {}\nTiros tomados: {}\nPessoas que fugiram: {}.".format(jogador[0], jogador[1], jogador[2]))
            continuar = input("\nVOCÊ QUER CONTINUAR? (S/N) ")
            #se o jogador não quiser continuar jogando na rodada atual:
            if continuar  == "n" or continuar == "N":
                #os cérebros comidos na rodada são adicionados à pontuação geral do jogador:
                pontuacoes[player] += jogador[0]
                #exibindo a pontuação de cada jogador até o momento:
                print("\n===PONTUAÇÃO ATUAL:===")
                for i in range(len(players)):
                    print("{}: {}".format(players[i], pontuacoes[i]))
                time.sleep(1.5)
                #verificando se o jogador não venceu a partida:
                vencedor()
                #chamando o próximo jogador:
                player += 1
                #reiniciando as listas dados, dados sorteados, faces e jogador:
                dados = []
                dados = copo(dados)
                dados_sorteados = []
                faces_sorteadas = []
                jogador = [0, 0, 0]
                if player == len(players):
                    player = 0
                    continue 
            elif continuar == "s" or continuar == "S":
                '''adaptação em relação ao jogo original: aqui, se o jogador não se atentar à quantidade restante de dados, pode acabar ficando com 
                menos de 3 dados para sortear e, assim, "quebrar" o jogo'''
                print("Você é fominha, hein, {}?\nÉ melhor fazer meu tempo valer a pena. Vamos lá!\n\nPERA AÍ!\nVocê só tem {} dados!\nSe ficar com menos de 3 dados, você quebra o jogo e prejudica todo mundo!".format(players[player], len(dados)))
                dados_sorteados = []
                faces_sorteadas = []
         