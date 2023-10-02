from database.models.Passageiro import Passageiro
from database.models.Corrida import Corrida
from database.models.Motorista import Motorista

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")  


class PersonCLI(SimpleCLI):
    def __init__(self, driver_model):
        super().__init__()
        self.driver_model = driver_model
        self.add_command("create", self.create_passenger)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_driver)
        self.add_command("delete", self.delete_driver)
      

    def create_passenger(self):
        print("INSIRA AS INFORMAÇÕES DO PASSAGEIRO:")
        nome_passageiro = input("Entre com nome do passageiro: ")
        doc = input("Entre o numero do documento: ")
        passageiro = Passageiro(nome_passageiro, doc)

        print("INSIRA AS INFORMAÇÕES DO MOTORISTA: ")
        nota_motorista = input("Entre com a nota do motorista: ")
        motorista = Motorista(nota_motorista)
       
        print("INSIRA AS INFORMAÇÕES DAS CORRIDAS:")
        numero_corridas = int(input("Quantas corridas: "))

        for _ in range(numero_corridas):
            nota_corrida = input("Nota: ")
            dist = input("Distancia: ")
            valor = input("Valor: ")
            corrida = Corrida(nota_corrida, dist, valor, passageiro)
            motorista.adicionar_corrida(corrida)

        self.driver_model.create(passageiro, motorista, corrida)

    def read_driver(self):
        id = input("Insira o ID: ")
        driver = self.driver_model.read_by_id(id)

    def update_driver(self):
        id = input("Insira o ID do motorista que deseja atualizar: ")
        nova_nota = input("Insira a nova nota do motorista: ")
        self.driver_model.update_driver(id,nova_nota)



    def delete_driver(self):
        id = input("Insira o ID: ")
        self.driver_model.delete_driver(id)
       