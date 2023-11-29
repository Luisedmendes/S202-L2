from jogador import Jogador


class JogadorManager:
    def __init__(self, database):
        self.db = database

    def cadastrar_jogador(self):
        name = input("Digite o nome do jogador: ")
        overall = int(input("Digite o overall do jogador: "))
        rightfoot = input("Digite o pé preferido do jogador (Direito ou Esquerdo): ")
        leftfoot = input("Digite o pé não preferido do jogador (Direito ou Esquerdo): ")

        jogador = Jogador(name, overall, rightfoot, leftfoot)
        self.salvar_jogador(jogador)

        print("Jogador cadastrado com sucesso!")

    def salvar_jogador(self, jogador):
        query = """
            CREATE (j:Jogador {name: $name, overall: $overall, rightfoot: $rightfoot, leftfoot: $leftfoot})
        """
        parameters = jogador.__dict__
        self.db.execute_query(query, parameters)

    def listar_jogadores(self):
        
        query = """
            MATCH (j:Jogador)
            RETURN j.name AS name, j.overall AS overall, j.rightfoot AS rightfoot, j.leftfoot AS leftfoot
        """
        result = self.db.execute_query(query)

        if result:
            for record in result:
                name = record['name']
                overall = record['overall']
                rightfoot = record['rightfoot']
                leftfoot = record['leftfoot']

                jogador = Jogador(name, overall, rightfoot, leftfoot)

                print("Nome: ", jogador.name)
                print("Overall: ", jogador.overall)
                print("Pé Preferido: ", jogador.rightfoot)
                print("Pé Não Preferido: ", jogador.leftfoot)
                print("-----")
        else:
            print("Nenhum jogador encontrado.")

    def deletar_jogador(self):
        jogador_name = input("Digite o nome do jogador que deseja deletar: ")
        jogador = self.buscar_jogador(jogador_name)

        if jogador:
            self.remover_relacionamentos_jogador(jogador)
            self.remover_jogador(jogador)
            print(f"Jogador '{jogador.name}' deletado com sucesso!")
        else:
            print("Jogador não encontrado.")

    def buscar_jogador(self, jogador_name):
        query = """
            MATCH (j:Jogador {name: $jogador_name})
            RETURN j
        """
        parameters = {'jogador_name': jogador_name}
        result = self.db.execute_query(query, parameters)
        if result:
            return Jogador(**result[0]['j'])
        else:
            return None

    def remover_relacionamentos_jogador(self, jogador):
        query = """
            MATCH (j:Jogador {name: $jogador_name})-[r]-()
            DELETE r
        """
        parameters = {'jogador_name': jogador.name}
        self.db.execute_query(query, parameters)

    def remover_jogador(self, jogador):
        query = """
            MATCH (j:Jogador {name: $jogador_name})
            DELETE j
        """
        parameters = {'jogador_name': jogador.name}
        self.db.execute_query(query, parameters)

    def atualizar_jogador(self):
        jogador_name = input("Digite o nome do jogador que deseja atualizar: ")
        jogador = self.buscar_jogador(jogador_name)

        if jogador:
            new_name = input("Digite o novo nome do jogador: ")
            new_overall = int(input("Digite o novo overall do jogador: "))
            new_rightfoot = input("Digite o novo pé preferido do jogador (Direito ou Esquerdo): ")
            new_leftfoot = input("Digite o novo pé não preferido do jogador (Direito ou Esquerdo): ")

            jogador.name = new_name
            jogador.overall = new_overall
            jogador.rightfoot = new_rightfoot
            jogador.leftfoot = new_leftfoot

            self.atualizar_jogador_no_banco(jogador)
            print(f"Jogador '{jogador_name}' atualizado com sucesso!")
        else:
            print("Jogador não encontrado.")

    def atualizar_jogador_no_banco(self, jogador):
        query = """
            MATCH (j:Jogador {name: $jogador_name})
            SET j.name = $new_name,
                j.overall = $new_overall,
                j.rightfoot = $new_rightfoot,
                j.leftfoot = $new_leftfoot
        """
        parameters = {
            'jogador_name': jogador.name,
            'new_name': jogador.name,
            'new_overall': jogador.overall,
            'new_rightfoot': jogador.rightfoot,
            'new_leftfoot': jogador.leftfoot
        }
        self.db.execute_query(query, parameters)
    
        

    