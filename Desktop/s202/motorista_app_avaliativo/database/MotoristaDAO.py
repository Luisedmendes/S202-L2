from pymongo import MongoClient
from bson.objectid import ObjectId
from database.models.Passageiro import Passageiro
from database.models.Corrida import Corrida
from database.models.Motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create(self, passageiro: Passageiro, motorista: Motorista, corrida: Corrida):
        try:
          
            motorista_doc = {
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": c.nota,
                        "distancia": c.distancia,
                        "valor": c.valor,
                        "passageiro": {
                            "nome": passageiro.nome,
                            "documento": passageiro.documento
                        }
                    } for c in motorista.corridas
                ]
            }

            motorista_res = self.db.collection.insert_one(motorista_doc)
            motorista_id = motorista_res.inserted_id

            print(f"Motorista created with id: {motorista_id}")

            return motorista_id
        except Exception as e:
            print(f"An error occurred while creating records: {e}")
            return None

    def read_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Driver found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None    
        

    def update_driver(self, id: str, nova_nota: str):
        try:
            # Atualize a nota do motorista no banco de dados
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nota": nova_nota}}
            )

            if res.modified_count > 0:
                return res.modified_count
            else:
                return 0  
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None


    def delete_driver(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Driver deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None