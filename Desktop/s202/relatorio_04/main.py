from ProductAnalyzer import ProductAnalyzer

pd = ProductAnalyzer()

pd.sales_per_day()
pd.best_selling_product()
pd.customer_wtih_more_money_spent()
pd.products_with_more_sales()


#1.Média de gasto total:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])

#writeAJson(result, "Média de gasto total")

# Cliente que mais comprou em cada dia:
#result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

#writeAJson(result, "Cliente que mais comprou em cada dia")

# # Produto mais vendido:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
#    {"$sort": {"total": -1}},
#    {"$limit": 1}
#])

#writeAJson(result, "Produto mais vendido")

