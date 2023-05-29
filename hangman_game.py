def play_hangman():

    

    print("\033[33m-=-" * 8)
    print("\033[34m   JOGO DA FORCA!")
    print("\033[33m-=-" * 8)

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    

    enforcou = False
    acertou = False
    erros = 0 

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ").upper().strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1

        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        print("Parabéns, você ganhou")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")


if __name__ == "__main__":
    play_hangman()