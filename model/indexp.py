#!C:\Users\andre\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type:text/html\n")
print("Python Mongo")


import pymongo

connection=pymongo.MongoClient("mongodb://localhost:27017/")
#print(connection.list_database_names())

db=connection["taxi_kompanija"]
mycol=db["vraboteni"]
myData = { "ime":"Biljana", "prezime":"Andreeva" }
mycol.insert_one(myData)
