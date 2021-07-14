import pymongo
from bson.objectid import ObjectId
class Database:
    database_name="taxi_kompanijaCOPY"
    connection=""
    def __init__(self):
        self.connection=pymongo.MongoClient("mongodb://localhost:27017/")
        
    def insertDocument(self,collection_name,collection_document):
        db=self.connection[self.database_name]
        mycol=db[collection_name]
        mycol.insert_one(collection_document)
        
    def deleteDocument(self,collection_name,collection_document):
        db=self.connection[self.database_name]
        mycol=db[collection_name]
        mycol.delete_one(collection_document) 

    def deleteDocumentById(self,collection_name,_id):
        db=self.connection[self.database_name]
        mycol=db[collection_name]
        mycol.delete_one({'_id':ObjectId(_id)})        
    
    def editDocument(self,collection_name,filters,collection_document):
        db=self.connection[self.database_name]
        mycol=db[collection_name]
        mycol.update_one(filters,{"$set":collection_document}) 
        
    def selectDocumentReturn(self,collection_name):
        db=self.connection[self.database_name]
        mycol=db[collection_name]
        return mycol