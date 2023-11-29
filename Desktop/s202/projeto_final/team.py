class Team:
    def __init__(self, name):
        self.name = name
        self.jogadores = []



    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
