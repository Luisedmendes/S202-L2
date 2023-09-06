from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()