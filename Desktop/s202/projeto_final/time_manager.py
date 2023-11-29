from team import Team

class TeamManager:
    def __init__(self, database):
        self.db = database

    def cadastrar_time(self):
        name = input("Digite o nome do time: ")
        team = Team(name)
        self.salvar_time(team)
        print(f"Time '{team.name}' cadastrado com sucesso!")

    def salvar_time(self, team):
        query = """
            CREATE (t:Team {name: $name})
        """
        parameters = {'name': team.name }
        self.db.execute_query(query, parameters)

    def listar_times(self):
        query = """
            MATCH (t:Team)
            RETURN t.name AS name
        """
        result = self.db.execute_query(query)

        if result:
            for record in result:
                name = record['name']
             

                team = Team(name)
              

                print("Nome: ", team.name)
              
                print("-----")
        else:
            print("Nenhum time encontrado.")

    def deletar_time(self):
        team_name = input("Digite o nome do time que deseja deletar: ")
        team = self.buscar_time(team_name)

        if team:
            self.remover_time(team)
            print(f"Time '{team.name}' deletado com sucesso!")
        else:
            print("Time não encontrado.")

    
    def remover_time(self, team):
        query = """
            MATCH (t:Team {name: $team_name})
            DELETE t
        """
        parameters = {'team_name': team.name}
        self.db.execute_query(query, parameters)

    def buscar_time(self, team_name):
        query = """
            MATCH (t:Team {name: $team_name})
            RETURN t.name AS name
        """
        parameters = {'team_name': team_name}
        result = self.db.execute_query(query, parameters)
        if result:
            return Team(name=result[0]['name'])
        else:
            return None

    


    def remover_jogador_do_time(self, team, jogador):
        query = """
            MATCH (t:Team {name: $team_name})-[r:TEM_JOGADOR]->(j:Jogador {name: $jogador_name})
            DELETE r
        """
        parameters = {'team_name': team.name, 'jogador_name': jogador.name}
        self.db.execute_query(query, parameters)

    def atualizar_time_no_banco(self, time):
        query = """
            MATCH (t:Team {name: $team_name})
            SET t.name = $new_name
            
        """
        parameters = {
            'team_name': time.name,
            'new_name': time.name,
        }
        self.db.execute_query(query, parameters)

  