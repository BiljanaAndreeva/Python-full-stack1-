#!C:\Users\andre\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type:text/html\n")

import database
DataBase=database.Database
import sys
import json
data=json.load(sys.stdin)
from bson.objectid import ObjectId
from datetime import datetime

class ModelFiksniTrosoci(DataBase):

    collection_name="fiksniTrosoci"
    #konstruktor na model vraboteni       
    def __init__(self):
        #konstruktor na DataBase se povrzuva so rditelot   
        DataBase.__init__(self)
    
    def insertFix(self,kirija,smetkovoditel,banka,komunikaciski_uslugi,drug_trosokF,cenaF,data):
        trosokDocument={"kirija":kirija,"smetkovoditel":smetkovoditel,"banka":banka,"komunikaciski_uslugi":komunikaciski_uslugi,"drug_trosokF":drug_trosokF,"cenaF":cenaF,"data":data}
        DataBase.insertDocument(self,self.collection_name,trosokDocument)
        
    def deleteFixId(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)    
        
    def editFix(self,kirija,smetkovoditel,banka,komunikaciski_uslugi,drug_trosokF,cenaF,data):
        myFilter={"_id":_id}
        trosokDocument= {"kirija":kirija}
        DataBase.editDocument(self,self.collection_name,myFilter,trosokDocument)
        
    def selectFix(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)    

 
objFiksniTrosoci=ModelFiksniTrosoci() 

action=data[0]["action"]
#print(data[0]["action"])
if action=="insert":
        objFiksniTrosoci.insertFix(data[0]["kirija"],data[0]["smetkovoditel"],data[0]["banka"],data[0]["komunikaciski_uslugi"],data[0]["drug_trosokF"],data[0]["cenaF"],datetime.now())
elif action=="edit":   
        objFiksniTrosoci.editFix(data[0]["vraboteni"],data[0]["vozila"])
elif action=="delete":
        objFiksniTrosoci.deleteFixId(data[0]["pk_value"])
elif action=="create":
        dataJSON={}
        dataJSON["fiksniTrosoci_records"]=[]
        record=objFiksniTrosoci.selectFix()
        

        for y in record.find():
            print(y)
      
            dataJSON["fiksniTrosoci_records"].append(
                { "_id":str(y['_id']),
                  "kirija":y["kirija"],
                  "smetkovoditel":y["smetkovoditel"],
                  "banka":y["banka"],
                  "komunikaciski_uslugi":y["komunikaciski_uslugi"],
                  "drug_trosokF":y["drug_trosokF"],
                  "cenaF":y["cenaF"],
                  "data":str(y["data"])
                })
           
        with open('json/fiksniTrosoci.json','w') as outfile:
            json.dump(dataJSON,outfile)
            print(y)    