from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

class ProductAnalyzer:

    def sales_per_day(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group":{"_id":"$data_compra", "total_vendas":{"$sum":1}}}

        ])
        writeAJson(result, "Vendas por dia")

    def best_selling_product(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    def customer_wtih_more_money_spent(self):
        result = db.collection.aggregate([{"$unwind": "$produtos"},
        {"$group": {"_id":"$cliente_id","total_gasto":{"$sum": {"$multiply":["$produtos.quantidade","$produtos.preco"]}}}},
        {"$sort":{"total_gasto": -1}},
        {"$limit": 1}
        ])
        writeAJson(result, "Cleinte que mas gastou")

    def products_with_more_sales(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match" : {"produtos.quantidade": {"$gt": 1}}},
            {"$group":{"_id": "$produtos.descricao"}}
        ])
        writeAJson(result, "Produtos que tiveraum uma quantidade vendida acima de 1")