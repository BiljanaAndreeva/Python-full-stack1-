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

class ModelTrosokVraboten(DataBase):

    collection_name="trosokVraboten"
    #konstruktor na model vraboteni       
    def __init__(self):
        #konstruktor na DataBase se povrzuva so rditelot   
        DataBase.__init__(self)
        
    def insertTrosokVrabotenJSON(self,Document):
        DataBase.insertDocument(self,self.collection_name,Document)    
    
    def insertTrosokVraboten(self,vraboteni,plata,pridonesi,drug_Trosok,Cena,data):
        trosokVrabotenDocument = {"vraboteni":ObjectId(vraboteni),"plata":plata,"pridonesi":pridonesi,"drug_Trosok":drug_Trosok,"Cena":Cena,"data":data}
        DataBase.insertDocument(self,self.collection_name,trosokVrabotenDocument)
        
    def deleteTrosokVraboten(self,vraboteni,plata,pridonesi,drug_Trosok,Cena,data):
        trosokVrabotenDocument = {"vraboteni":vraboteni,"plata":plata,"pridonesi":pridonesi,"drug_Trosok":drug_Trosok,"Cena":Cena,"data":data}
        DataBase.deleteDocument(self,self.collection_name,trosokVrabotenDocument)
        
    def deleteTrosokVrabotenById(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)    
        
    def editTrosokVraboten(self,_id):
        myFilter={"_id":_id}
        trosokVrabotenDocument= {"drug_Trosok":drug_Trosok}
        DataBase.editDocument(self,self.collection_name,myFilter,trosokVrabotenDocument)
        
    def selectTrosokVraboten(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)
        
    def selectVraboteni(self):
        return DataBase.selectDocumentReturn(self,"vraboteni")    
        
        
#print(data)    
objTrosokVraboten=ModelTrosokVraboten()

action=data[0]["action"]
print(action)
if action=="insert":
    data[0]["data"]=str(datetime.now())
#    objTrosokVraboten.insertTrosokVrabotenJSON(data[0])
    objTrosokVraboten.insertTrosokVraboten(data[0]["vraboteni"],data[0]["plata"],data[0]["pridonesi"],data[0]["drug_Trosok"],data[0]["Cena"],datetime.now())
elif action=="edit":   
    objTrosokVraboten.editTrosokVraboten(data[0]["_id"],data[0]["drug_Trosok"])
elif action=="delete":
    #objTrosokVraboten.deleteTrosokVraboten(data[0]["vraboteni"])
    objTrosokVraboten.deleteTrosokVrabotenById(data[0]["pk_value"])
elif action=="create":
    dataJSON={}
    dataJSON['trosokVraboten_records']=[]
    record=objTrosokVraboten.selectTrosokVraboten()
    vraboteni_records=objTrosokVraboten.selectVraboteni()
    for y in record.find():
        for vrb in vraboteni_records.find({"_id":ObjectId(y["vraboteni"])}):
            dataJSON['trosokVraboten_records'].append(
            { "_id":str(y['_id']),
            "ime":vrb["ime"],
            "prezime":str(vrb["prezime"]),
            "plata":str(y["plata"]),
            "pridonesi":str(y["pridonesi"]),
            "drug_Trosok":y["drug_Trosok"],
            "Cena":str(y["Cena"]),
            "data":str(y["data"])})
    
    with open('json/trosokVraboten.json','w') as outfile:
         json.dump(dataJSON,outfile)
         print(y)








