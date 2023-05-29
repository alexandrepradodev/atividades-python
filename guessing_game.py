from random import randint
from time import sleep

def play_guessing_game():

    secret_number = randint(1, 10)
    remaining_attempts = 0
    tries = 0 
    difficulty = 0 
    choices = (1, 2, 3) 
    points = 10

    def loading(x): # Função que define o carregamento, em segundos, das etapas do jogo.
        sleep(x)

    print("\033[33m-=-" * 8)
    print("\033[34m   JOGO DA ADVINHAÇÃO!")
    print("\033[33m-=-" * 8)
    loading(2)

    while difficulty not in choices:
        print("""\033[34m\nEscolha o nível de dificuldade: 

\033[32m(1) Fácil - 6 tentativas
\033[33m(2) Médio - 3 tentativas 
\033[31m(3) Difícil - 1 tentativa\033[m
        """)
        difficulty = input("Sua escolha: ").strip()
        if difficulty.isdigit():
            difficulty = int(difficulty)
            if difficulty == 1:
                remaining_attempts = 6
                print("\n\033[32mVocê escolheu a dificuldade fácil!")
                loading(2)
            elif difficulty == 2:
                remaining_attempts = 3
                print("\n\033[33mVocê escolheu a dificuldade média!")
                loading(2)
            elif difficulty == 3:
                remaining_attempts = 1 
                print("\n\033[31mVocê escolheu a dificuldade difícil!\033[m")

        else:    
            print("\n\033[31mDidite um número inteiro entre 1 e 3\033[m")
            loading(2)
            continue

    while True:
        user_name = input("\n\033[34mDigite o seu apelido ou nome:\033[m ").strip().capitalize()
        if user_name.isdigit():
            print("\n\033[31mDigite um nome composto apenas por letras ou com letras e números!\033[31m")
            continue
        else:
            break

    print(f"\n\033[33mSeja bem-vindo(a),\033[34m {user_name}\033[m!")
    loading(2)

    while remaining_attempts != 0:

        number_chosen_str = input("\n\033[33mTente adivinhar\033[m o número entre 1 e 10: ").strip()
        

        print(f"\n\033[33mChecando se o número {number_chosen_str} é o número secreto...\033[m")
        loading(2)
        
        if number_chosen_str.isdigit():

            number_chosen_int = int(number_chosen_str)
            lost_points = abs(secret_number - number_chosen_int)
            points -=  lost_points

            if number_chosen_int <= 10 and number_chosen_int >= 1:
                remaining_attempts -= 1
                tries += 1

                if (number_chosen_int == secret_number) and (tries == 1):
                    print(f"\nParabéns, {user_name}! \033[32mvocê acertou de primeira e fez {abs(points)} pontos de 10.\033[m")
                    break

                elif number_chosen_int == secret_number and tries > 1:
                    print(f"\nParabéns, {user_name}! \033[32mVocê acertou\033[m depois de {tries}",end= ' ')
                    print(f"tentativas e fez {abs(points)} pontos de 10.")
                    break

                elif number_chosen_int > secret_number:
                    print(f"\n\033[31mO número {number_chosen_int}\033[m é MAIOR que o número secreto.")

                elif number_chosen_int < secret_number:
                    print(f"\n\033[31mO número {number_chosen_int}\033[m é MENOR que o número secreto.")
                
            else: 
                print(f"\nO número\033 {number_chosen_int}\033[m não está entre 1 e 10")
                loading(2)

        else:
            print("\n\033[31mEscolha um número inteiro entre 1 e 10.\033[m")
            loading(2)
            continue

    if remaining_attempts == 0 and secret_number != number_chosen_int:
        print(f"\n\033[31mInfelizmente você não acertou!\033[m O número secreto era {secret_number}. Tente novamente quando quiser!")
        
    loading(2)
    print("\n\033[34mObrigado por jogar!")
    print(f"\nCriado por Alexandre do Prado\033[m")
        
if(__name__ == "__main__"):
    play_guessing_game()

