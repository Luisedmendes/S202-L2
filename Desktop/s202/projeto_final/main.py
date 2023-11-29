from database import Database
from menu import Menu

def main():
  db = Database(uri="bolt://18.210.7.218:7687", user="neo4j", password="possibilities-giants-abrasion")
  #db.drop_all()

  menu = Menu(db)
  menu.exibir_menu()

if __name__ == "__main__":
  main()  
  