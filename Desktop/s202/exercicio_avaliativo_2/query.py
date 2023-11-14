from database import Database

uri = "bolt://52.91.21.8:7687"
user = "neo4j"
password = "package-mate-hydrometers"



def questao_01():
    db = Database(uri,user,password)

    # 1. Busque pelo professor "Teacher" cujo nome seja "Renzo", retorne o ano_nasc e o CPF.
    query_1 = """
    MATCH (t:Teacher{name:'Renzo'})
    RETURN t.ano_nasc, t.cpf
    """

    db.drop
    result_1 = db.execute_query(query_1)
    print("Resultado 1:", result_1)

    # 2. Busque pelos professores "Teacher" cujo nome comece com a letra "M", retorne o name e o cpf.
    query_2 = """
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH 'M'
    RETURN t.name, t.cpf
    """
    result_2 = db.execute_query(query_2)
    print("Resultado 2:", result_2)

    # 3. Busque pelos nomes de todas as cidades "City" e retorne-os.
    query_3 = """
    MATCH (c:City)
    RETURN c.name
    """
    result_3 = db.execute_query(query_3)
    print("Resultado 3:", result_3)

    # 4. Busque pelas escolas "School", onde o number seja maior ou igual a 150 e menor ou igual a 550,
    # retorne o nome da escola, o endereço e o número.
    query_4 = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name, s.address, s.number
    """
    result_4 = db.execute_query(query_4)
    print("Resultado 4:", result_4)

    db.close()


def questao_02():
    db = Database(uri, user, password)

    # 1. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
    query_1 = """
    MATCH (t:Teacher)
    WITH MIN(t.ano_nasc) AS mais_jovem, MAX(t.ano_nasc) AS mais_velho
    RETURN mais_jovem, mais_velho
    """
    result_1 = db.execute_query(query_1)
    print("Resultado 1:", result_1)

    # 2. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade "population".
    query_2 = """
    MATCH (c:City)
    WITH AVG(c.population) AS media_habitantes
    RETURN media_habitantes
    """
    result_2 = db.execute_query(query_2)
    print("Resultado 2:", result_2)

    # 3. Encontre a cidade cujo CEP seja igual a "37540-000" e retorne o nome com todas as letras "a" substituídas por "A".
    query_3 = """
    MATCH (c:City{cep:'37540-000'})
    RETURN REPLACE(c.name, 'a', 'A') AS nome_substituido
    """
    result_3 = db.execute_query(query_3)
    print("Resultado 3:", result_3)

    # 4. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
    query_4 = """
    MATCH (t:Teacher)
    RETURN SUBSTRING(t.name, 2, 1) AS terceira_letra
    """
    result_4 = db.execute_query(query_4)
    print("Resultado 4:", result_4)

    db.close()

# Execute as queries da Questão 01
questao_01()

# Execute as queries da Questão 02
questao_02()
