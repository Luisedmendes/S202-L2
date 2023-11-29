from time_manager import TeamManager
from jogador_manager import JogadorManager

class Menu:
    
    def __init__(self, database):
        self.db = database
        self.jogador_manager = JogadorManager(database)
        self.time_manager = TeamManager(database)
        

    def exibir_menu(self):
        while True:
            print("1. Cadastrar Jogador")
            print("2. Listar Jogadores")
            print("3. Deletar Jogador")
            print("4. Atualizar Jogador")
            print("5. Cadastrar Time")
            print("6. Listar Times")
            print("7. Adicionar jogador ao time")
            print("8. Deletar time")
            print("9. Atualizar time")
            print("10. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.jogador_manager.cadastrar_jogador()
            elif opcao == "2":
                self.jogador_manager.listar_jogadores()
            elif opcao == "3":
                self.jogador_manager.deletar_jogador()
            elif opcao == "4":
                self.jogador_manager.atualizar_jogador()
            elif opcao == "5":
                self.time_manager.cadastrar_time()
            elif opcao == "6":
                self.time_manager.listar_times() # listar times
            elif opcao == "7":
                self.adicionar_jogador_ao_time() # adicionar jogador ao time
            elif opcao == "8":
                self.time_manager.deletar_time()
            elif opcao == "9":
                self.time_manager.atualizar_time_no_banco()
            elif opcao == "10":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_jogador_ao_time(self):
        time_name = input('Entre com nome do time: ')
        jogador_name = input('Entre com nome do time: ')
        team = self.time_manager.buscar_time(time_name)
        jogador = self.jogador_manager.buscar_jogador(jogador_name)

        if team and jogador:
            query = """
                MATCH (t:Team {name: $team_name}), (j:Jogador {name: $jogador_name})
                MERGE (t)-[:TEM_JOGADOR]->(j)
                WITH t, j
                SET t.jogadores = t.jogadores + j
            """
            parameters = {'team_name': team.name, 'jogador_name': jogador.name}
            self.db.execute_query(query, parameters)
            print(f"Jogador '{jogador.name}' adicionado ao time '{team.name}' com sucesso!")
        else:
            print("Time ou jogador não encontrado.")

            

