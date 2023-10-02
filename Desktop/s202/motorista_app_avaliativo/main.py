from database.database import Database
from cli import PersonCLI
from database.MotoristaDAO import MotoristaDAO

db = Database(database="app", collection="motoristas")#Arrumar no compass
motoristaModel = MotoristaDAO(database=db)

personCLI = PersonCLI(motoristaModel)
personCLI.run()