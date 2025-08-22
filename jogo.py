# Coloque todo o seu jogo dentro de um loop 'while'
jogar_novamente = 'sim'
while jogar_novamente.lower() == 'sim':
    print('''*******************************************************************************
          |                   |                   |                   |
 _________|________________.=""_;=.______________|_____________________|_______
|                           |  ,-"_,=""    `"=. |                   |
|___________________|__"=._o`"-._       `"=.______________|___________________
          |               `"=._o`"=._     _`"=._               |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                           |   __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._  ". '__|___________________
          |             |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                           | |o;     `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;    (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._      ; | ;      ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
    print("Bem-vindo à ilha do tesouro!")
    print("Sua missão é encontrar o tesouro perdido.")

    # Primeiro ponto de decisão
    print("\nVocê está em uma encruzilhada. Para onde você vai?")
    escolha1 = input("Digite 'esquerda' ou 'direita': ").lower()

    if escolha1 == 'esquerda':
        print("\nVocê chegou a um lago. Há uma ilha no meio.")
        escolha2 = input("Você nada até a ilha ou espera por um barco? Digite 'nadar' ou 'esperar': ").lower()

        if escolha2 == 'nadar':
            print("\nVocê é atacado por um crocodilo! Fim de jogo.")
        elif escolha2 == 'esperar':
            print("\nUm barco surge e te leva à ilha. Há três portas à sua frente.")
            escolha3 = input("Qual porta você escolhe? Digite 'vermelha', 'azul' ou 'amarela': ").lower()

            if escolha3 == 'vermelha':
                print("\nVocê encontra uma sala cheia de ouro! Você venceu!")
            elif escolha3 == 'azul':
                print("\nVocê cai em uma armadilha e é esmagado! Fim de jogo.")
            elif escolha3 == 'amarela':
                print("\nVocê é atacado por um grupo de macacos! Fim de jogo.")
            else:
                print("\nEscolha inválida. Fim de jogo.")
        else:
            print("\nEscolha inválida. Fim de jogo.")

    elif escolha1 == 'direita':
        print("\nVocê encontra uma floresta densa e se perde. Fim de jogo.")

    else:
        print("\nEscolha inválida. Fim de jogo.")

    # Pergunta ao jogador se ele quer jogar novamente
    print("\n" + "="*50)
    jogar_novamente = input("Deseja jogar novamente? Digite 'sim' ou 'não': ")
    print("="*50 + "\n")

print("Obrigado por jogar!")
