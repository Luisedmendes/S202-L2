from database import Database

class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.db = Database(uri, user, password)

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)


    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result[0] if result else None

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)

    def close_database(self):
        self.db.close()
        
