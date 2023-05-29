import hangman_game
import guessing_game
from time import sleep

def loading(x):
    sleep(x)
def choose_game():
    game = 0
    games = (1, 2)
    print("\033[33m-=-" * 8)
    print("\033[34m   ESCOLHA O SEU JOGO!")
    print("\033[33m-=-" * 8)

    print("""\033[33m
(1) Jogo da forca
(2) Jogo da advinhação\033[m
    """)
    loading(1)
    while game not in games:
        game = input("Qual jogo irá jogar? ").strip()

        if game.isdigit() and int(game) in games:
            game = int(game)
            if game == 1:
                print("\n\033[32mInicializando o jogo da forca...\033[m")
                print()
                loading(3)
                hangman_game.play_hangman()
                
            elif game == 2:
                print("\n\033[32mInicializando o jogo da advinhação...\033[m")
                print()
                loading(3)
                guessing_game.play_guessing_game()
                
        else:
            print("\nDigite 1 ou 2!")
            loading(2)

if(__name__ == "__main__"): # Essa linha de código serve para caso esse arquivo for importado ele não seja o principal lá
    choose_game()            
