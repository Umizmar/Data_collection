from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['DZ3']
collection = db.books

# for doc in collection.find({"available":3}):
#     print(doc)

# for doc in collection.find({"available":{"$gt":19}}):
#     print(doc)

# for doc in collection.find({'$or':[{"available":{"$gt":20}},{"price":{"$gt":55}}]}):
#      print(doc)

# for doc in collection.find({'title':{'$regex':'Sl.'}},{'description':0}).sort('price'):
#     print(doc)

# collection.update_one({'title':'Thinking, Fast and Slow'}, {'$set':{'title':'Thinking'}})

