import random

# Classe que representa o tabuleiro do jogo

class Tabuleiro:

# Inicializa o tabuleiro vazio
    def __init__(self):
        self.casas = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def pegar_tabuleiro(self):
        return [
            [self.casas[0], self.casas[1], self.casas[2]],
            [self.casas[3], self.casas[4], self.casas[5]],
            [self.casas[6], self.casas[7], self.casas[8]]
        ]
    
  # Marca uma casa no tabuleiro se estiver vazia
    def marcar_casa(self, posicao, simbolo):
        if self.casas[posicao] == ' ':
            self.casas[posicao] = simbolo
            return True
        else:
            return False
        
#Mostra o tabuleiro atual
    def imprimir_tabuleiro(self):
        tabuleiro = self.pegar_tabuleiro()
        print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")

# Classe base para os jogadores'
class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro):
        pass

# Classe para jogador humano0
class JogadorHumano(Jogador):
    def fazer_jogada(self, tabuleiro):
        while True:
            try:
                jogada = int(input(f"Jogador {self.simbolo}, escolha uma posição (0-8): "))
                if jogada >= 0 and jogada <= 8:
                    if tabuleiro.casas[jogada] == ' ':
                        return jogada
                    else:
                        print("Essa posição já foi ocupada!")
                else:
                    print("Número inválido! Escolha entre 0 e 8.")
            except ValueError:
                print("Por favor, digite um número válido.")

# Classe para jogador computador
class JogadorComputador(Jogador):
    def __init__(self, simbolo, estrategia="aleatoria"):
        super().__init__(simbolo)
        self.estrategia = estrategia

    def fazer_jogada(self, tabuleiro):
        if self.estrategia == "aleatoria":
            posicoes_vazias = []
            for i in range(9):
                if tabuleiro.casas[i] == ' ':
                    posicoes_vazias.append(i)
            return random.choice(posicoes_vazias)
        
# Classe principal do jogo
class JogoVelha:
    def __init__(self, jogador1, jogador2):
        self.jogadores = [jogador1, jogador2]
        self.tabuleiro = Tabuleiro()
        self.turno = 0

 # Imprime o tabuleiro inicial com posições numeradas para melhor visualização.
    def imprimir_tabuleiro_inicial(self):
        print("Tabuleiro inicial:")
        self.tabuleiro.imprimir_tabuleiro()
        print("\nPosições do tabuleiro:")
        print(" 0 | 1 | 2 ")
        print("---+---+---")
        print(" 3 | 4 | 5 ")
        print("---+---+---")
        print(" 6 | 7 | 8 ")

 # Retorna o jogador atual
    def jogador_atual(self):
        return self.jogadores[self.turno % 2]
    
 # Verifica se o jogo terminou
    def checar_fim_de_jogo(self):
        
        for i in range(0, 9, 3):
            if self.tabuleiro.casas[i] == self.tabuleiro.casas[i+1] == self.tabuleiro.casas[i+2] != ' ':
                return f"Jogador {self.tabuleiro.casas[i]} venceu!"

        
        for i in range(3):
            if self.tabuleiro.casas[i] == self.tabuleiro.casas[i+3] == self.tabuleiro.casas[i+6] != ' ':
                return f"Jogador {self.tabuleiro.casas[i]} venceu!"

        
        if self.tabuleiro.casas[0] == self.tabuleiro.casas[4] == self.tabuleiro.casas[8] != ' ':
            return f"Jogador {self.tabuleiro.casas[0]} venceu!"
        if self.tabuleiro.casas[2] == self.tabuleiro.casas[4] == self.tabuleiro.casas[6] != ' ':
            return f"Jogador {self.tabuleiro.casas[2]} venceu!"

        
        if ' ' not in self.tabuleiro.casas:
            return "Empate!"

        return None
    
# Executa o loop principal do jogo
    def jogar(self):
        self.imprimir_tabuleiro_inicial()
        
        while True:
            jogador = self.jogador_atual()
            jogada = jogador.fazer_jogada(self.tabuleiro)
            
            if self.tabuleiro.marcar_casa(jogada, jogador.simbolo):
                print(f"Jogador {jogador.simbolo} jogou na posição {jogada}")
                self.tabuleiro.imprimir_tabuleiro()
                
                resultado = self.checar_fim_de_jogo()
                if resultado:
                    print(resultado)
                    break
                
                self.turno += 1
            else:
                print("Jogada inválida, Tente novamente.")