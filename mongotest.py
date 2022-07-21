import pymongo
client = pymongo.MongoClient("mongodb+srv://HumeraNaz:KdAXfqeNeg2wPWhz@cluster0.nopgagn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"Humera",
    "Email":"humeranaz911@gmail.com",
    "surname":"Naz"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)