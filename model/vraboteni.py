#!C:\Users\andre\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type:text/html\n")

import database   #ova e filename.py(Database.py)
#my var=filename.classname
DataBase=database.Database
import sys
import json
data=json.load(sys.stdin)
from bson.objectid import ObjectId
from datetime import datetime

class ModelVraboteni(DataBase):

    collection_name="vraboteni"
    #konstruktor na model vraboteni       
    def __init__(self):
        #konstruktor na DataBase se povrzuva so rditelot   
        DataBase.__init__(self)
    
    def insertVraboteni(self,ime,prezime):
        #tipot na dokumentot ime-var.,prezime-varable  
        #"ime"-property,"prezime"-property
        vraboteniDocument = {"ime":ime, "prezime":prezime }
        #insert so parent                     vraboteni      ,     tip na dokumentot
        DataBase.insertDocument(self,self.collection_name,vraboteniDocument)
        
    def deleteVraboteni(self,ime,prezime):
        vraboteniDocument = {"ime":ime, "prezime":prezime }
        DataBase.deleteDocument(self,self.collection_name,vraboteniDocument)
        
    def deleteVraboteniById(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)    
        
    def editVraboteni(self,_id,prezime):
        myFilter={"_id":ObjectId(_id)}
        vraboteniDocument = {"prezime":prezime}
        DataBase.editDocument(self,self.collection_name,myFilter,vraboteniDocument)
        
    def selectVraboteni(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)
        
        
#print(data)    
objVraboteni=ModelVraboteni()

action=data[0]["action"]
print(action)
if action=="insert":
    objVraboteni.insertVraboteni(data[0]["ime"],data[0]["prezime"])
elif action=="edit":   
    objVraboteni.editVraboteni(data[0]["pk_value"],data[0]["prezime"])
elif action=="delete":
    #objVraboteni.deleteVraboteni(data[0]["ime"],data[0]["prezime"])
    objVraboteni.deleteVraboteniById(data[0]["pk_value"])
elif action=="create":
    dataJSON={}
    dataJSON['vraboteni_records']=[]
    record=objVraboteni.selectVraboteni()
    for y in record.find():
     dataJSON['vraboteni_records'].append({ "_id":str(y['_id']),"ime":y["ime"],"prezime":y["prezime"]})
    
    with open('json/vraboteni.json','w') as outfile:
        json.dump(dataJSON,outfile)
        print(y)
#objVraboteni.insertVraboteni("Elena","Filipova")
#objVraboteni.deleteVraboteni("Elena","Filipova")
#objVraboteni.editVraboteni("Biljana","Dzurovska-Andreeva")'''








