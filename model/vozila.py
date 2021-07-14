#!C:\Users\andre\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type:text/html\n")


import database   #ova e filename.py(Database.py)
#my var=filename.classname
DataBase=database.Database
import sys
import json
data=json.load(sys.stdin)
from bson.objectid import ObjectId
    
class ModelVozila(DataBase):

    collection_name="vozila"
    def __init__(self): 
        DataBase.__init__(self)
    def insertVozila(self,ime_vozilo,broj_vozilo):
        vozilaDocument= {"ime_vozilo":ime_vozilo,"broj_vozilo":broj_vozilo}
        DataBase.insertDocument(self,self.collection_name,vozilaDocument)
        
    def deleteVozila(self,ime_vozilo,broj_vozilo):
        myData= {"ime_vozilo":ime_vozilo,"broj_vozilo":broj_vozilo}
        DataBase.deleteDocument(self,self.collection_name,myData)

    def deleteVozilaById(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)

    def editVozila(self,_id,ime_vozilo):
        myFilter={"_id":ObjectId(_id)}
        vozilaDocument = {"ime_vozilo":ime_vozilo}
        DataBase.editDocument(self,self.collection_name,myFilter,vozilaDocument)   
    
    def selectVozila(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)
        
print(data)        
objVozila=ModelVozila()

action=data[0]["action"]

if action=="insert":
    objVozila.insertVozila(data[0]["ime_vozilo"],data[0]["broj_vozilo"])
elif action=="edit":   
    objVozila.editVozila(data[0]["pk_value"],data[0]["ime_vozilo"])
elif action=="delete":
    #objVozila.deleteVozila(data[0]["ime_vozilo"],data[0]["broj_vozilo"])
    objVozila.deleteVozilaById(data[0]["pk_value"])
elif action=="create":
    dataJSON={}
    dataJSON['vozila_records']=[]
    record=objVozila.selectVozila()
    for y in record.find():
     dataJSON['vozila_records'].append({ "_id":str(y['_id']),"ime_vozilo":y["ime_vozilo"],"broj_vozilo":y["broj_vozilo"]})
    with open('json/vozila.json','w') as outfile:
        json.dump(dataJSON,outfile)
        print(y)    
#objVozila.insertVozila("Hundai i 20",4)
#objVozila.deleteVozila("Renaut Megan 2",42)