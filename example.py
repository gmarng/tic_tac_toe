from jogovelha import JogoVelha, JogadorHumano, JogadorComputador

if __name__ == "__main__":
    jogador1 = JogadorHumano('X')
    jogador2 = JogadorComputador('O')
    jogo = JogoVelha(jogador1, jogador2)
    jogo.jogar()