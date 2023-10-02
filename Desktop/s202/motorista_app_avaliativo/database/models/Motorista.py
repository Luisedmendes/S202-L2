class Motorista:
    def __init__(self, nota):
        self.nota = nota
        self.corridas = []  

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)
