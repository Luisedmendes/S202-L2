from database import Database
from writeAJson import writeAJson
from personModel import PersonModel
from cli import PersonCLI

db = Database(database="relatorio_05", collection="livros")
personModel = PersonModel(database=db)


personCLI = PersonCLI(personModel)
personCLI.run()