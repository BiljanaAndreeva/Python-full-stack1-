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

class ModelTrosokVozilo(DataBase):

    collection_name="trosokVozilo"
    #konstruktor na model vraboteni       
    def __init__(self):
        #konstruktor na DataBase se povrzuva so rditelot   
        DataBase.__init__(self)
        
    def insertTrosokVoziloJSON(self,Document):
        DataBase.insertDocument(self,self.collection_name,Document)    
    
    def insertTrosokVozilo(self,vozila,gorivo,drug_trosok,cena,data):
        #tipot na dokumentot ime-var.,prezime-varable  
        #"ime"-property,"prezime"-property
        trosokVoziloDocument = {"vozila":ObjectId(vozila),"gorivo":gorivo,"drug_trosok":drug_trosok,"cena":cena,"data":data}
        #insert so parent                     vraboteni      ,     tip na dokumentot
        DataBase.insertDocument(self,self.collection_name,trosokVoziloDocument)
        
    def deleteTrosokVozilo(self,vozila,gorivo,drug_trosok,cena,data):
        trosokVoziloDocument = {"vozila":vozila, "gorivo":gorivo,"drug_trosok":drug_trosok,"cena":cena}
        DataBase.deleteDocument(self,self.collection_name,trosokVoziloDocument)
        
    def deleteTrosokVoziloById(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)    
        
    def editTrosokVozilo(self,_id):
        myFilter={"_id":_id}
        trosokVoziloDocument= {"gorivo":gorivo}
        DataBase.editDocument(self,self.collection_name,myFilter,trosokVoziloDocument)
        
    def selectTrosokVozilo(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)
        
    def selectVozila(self):
        return DataBase.selectDocumentReturn(self,"vozila")    
        
        
#print(data)    
objTrosokVozilo=ModelTrosokVozilo()

action=data[0]["action"]
print(action)
if action=="insert":
    data[0]["data"]=str(datetime.now())
#    objTrosokVozilo.insertTrosokVoziloJSON(data[0])
    objTrosokVozilo.insertTrosokVozilo(data[0]["vozila"],data[0]["gorivo"],data[0]["drug_trosok"],data[0]["cena"],datetime.now())
elif action=="edit":   
    objTrosokVozilo.editTrosokVozilo(data[0]["_id"],data[0]["gorivo"])
elif action=="delete":
    #objTrosokVozilo.deleteTrosokVozilo(data[0]["ime"],data[0]["prezime"])
    objTrosokVozilo.deleteTrosokVoziloById(data[0]["pk_value"])
elif action=="create":
    dataJSON={}
    dataJSON['trosokVozilo_records']=[]
    record=objTrosokVozilo.selectTrosokVozilo()
    vozila_record=objTrosokVozilo.selectVozila()
    for y in record.find():
        for vozila in vozila_record.find({"_id":ObjectId(y["vozila"])}):
            dataJSON['trosokVozilo_records'].append(
            { "_id":str(y['_id']),
            "ime_vozilo":vozila["ime_vozilo"],
            "broj_vozilo":str(vozila["broj_vozilo"]),
            "gorivo":str(y["gorivo"]),
            "drug_trosok":y["drug_trosok"],
            "cena":str(y["cena"]),
            "data":str(y["data"])})
    
    with open('json/trosokVozilo.json','w') as outfile:
        json.dump(dataJSON,outfile)
        print(y)
#objVraboteni.insertVraboteni("Elena","Filipova")
#objVraboteni.deleteVraboteni("Elena","Filipova")
#objVraboteni.editVraboteni("Biljana","Dzurovska-Andreeva")'''








