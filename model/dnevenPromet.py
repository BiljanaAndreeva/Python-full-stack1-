#!C:\Users\andre\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type:text/html\n")

import database
DataBase=database.Database
import sys
import json
data=json.load(sys.stdin)
from bson.objectid import ObjectId
from datetime import datetime

class ModelDnevenPromet(DataBase):

    collection_name="dnevenPromet"
    #konstruktor na model vraboteni       
    def __init__(self):
        #konstruktor na DataBase se povrzuva so rditelot   
        DataBase.__init__(self)
    
    def insertDnevenPrometJSON(self,Document):
        DataBase.insertDocument(self,self.collection_name,Document)
    
    def insertDnevenPromet(self,vraboteni,vozila,pocetni_km,krajni_km,prazni_km,dopolnitelen_trosok,data_promet):
        DnevenPrometDocument={"vraboteni":ObjectId(vraboteni),"vozila":ObjectId(vozila),"pocetni_km":pocetni_km,"krajni_km":krajni_km,"prazni_km":prazni_km,dopolnitelen_trosok:"dopolnitelen_trosok","data_promet":data_promet}
        DataBase.insertDocument(self,self.collection_name,DnevenPrometDocument)
        
    def deleteDnevenPrometById(self,_id):
        DataBase.deleteDocumentById(self,self.collection_name,_id)    
        
    def editDnevenPromet(self,_id,pocetni_km,krajni_km,prazni_km):
        myFilter={"_id":ObjectId(_id)}
        DnevenPrometDocument = {"pocetni_km":pocetni_km,"krajni_km":krajni_km,"prazni_km":prazni_km}
        DataBase.editDocument(self,self.collection_name,myFilter,DnevenPrometDocument)
        
    def selectDnevenPromet(self):
        return DataBase.selectDocumentReturn(self,self.collection_name)    

    def selectVraboteni(self):
        return DataBase.selectDocumentReturn(self,"vraboteni")

    def selectVozila(self):
        return DataBase.selectDocumentReturn(self,"vozila")
        
    def totalKM(self,km_start,km_end):
        total=0
        total=km_end-km_start
        return total
        
    def prometVk(self,km_start,km_end):
        promet=0
        promet=(km_end-km_start)*18
        return promet
        
    def prometFirma(self,km_start,km_end):
        promet_firma=0
        promet_firma=(((km_end-km_start)*18)/100)*75
        return promet_firma
        
    def prometVraboten(self,km_start,km_end):
        promet_vraboten=0
        promet_vraboten=(((km_end-km_start)*18)/100)*25
        return promet_vraboten  

def totalPrice(priceByProduct) :
        total=0
        total=total+priceByProduct
        return total
 
objDnevenPromet=ModelDnevenPromet() 

action=data[0]["action"]
print(data[0])
if action=="insert":
        #print(datetime.now().year)
        #data[0]={"data_promet":"pp"}
        #print(data[0])
        data[0]["data_promet"]=str(datetime.now())
        objDnevenPromet.insertDnevenPrometJSON(data[0])
        #objDnevenPromet.insertDnevenPromet(data[0]["vraboteni"],data[0]["vozila"],data[0]["pocetni_km"],data[0]["krajni_km"],data[0]["prazni_km"],datetime.now())
elif action=="edit":   
        objDnevenPromet.editDnevenPromet(data[0]["pk_value"],data[0]["pocetni_km"],data[0]["krajni_km"],data[0]["prazni_km"])
elif action=="delete":
        objDnevenPromet.deleteDnevenPrometById(data[0]["pk_value"])
elif action=="create":
        opis=0
        cena=0
        aktivni_km=0
        promet=0
        
        dataJSON={}
        dataJSON["dnevenPromet_records"]=[]
        record=objDnevenPromet.selectDnevenPromet()
        vraboteni_record=objDnevenPromet.selectVraboteni()
        vozila_record=objDnevenPromet.selectVozila()

        for y in record.find():
            total_price=0
            #print(y)
            for vr in vraboteni_record.find({"_id":ObjectId(y["vraboteni"])}):
                for vozila in vozila_record.find({"_id":ObjectId(y["vozila"])}):
                    
                    #totalp=total(y["pocetni_km"],y["pocetni_km"])     
                    dataJSON["dnevenPromet_records"].append(
                        { "_id":str(y['_id']),
                        "ime":vr["ime"],
                        "prezime":vr["prezime"],
                        "ime_vozilo":vozila["ime_vozilo"],
                        "broj_vozilo":str(vozila["broj_vozilo"]),
                        "pocetni_km":y["pocetni_km"],
                        "krajni_km":y["krajni_km"],
                        "prazni_km":y["prazni_km"],
                        "aktivni_km":objDnevenPromet.totalKM(int(y["pocetni_km"]),int(y["krajni_km"])),
                        "promet":objDnevenPromet.prometVk(int(y["pocetni_km"]),int(y["krajni_km"])),
                        "promet_firma":objDnevenPromet.prometFirma(int(y["pocetni_km"]),int(y["krajni_km"])),
                        "promet_vraboten":objDnevenPromet.prometVraboten(int(y["pocetni_km"]),int(y["krajni_km"])),
                        "total_price":0,
                        "data_promet":str(y["data_promet"]),
                        "dopolnitelen_trosok":[]
                       #"total_tax":0
                    })
                    for sumTrosoci in y["dopolnitelen_trosok"]:
                        total_price=total_price+int(sumTrosoci["cena"])
                        dataJSON["dnevenPromet_records"][len(dataJSON["dnevenPromet_records"])-1]["dopolnitelen_trosok"].append(
                        {"opis":sumTrosoci["opis"],
                         "cena":sumTrosoci["cena"]})
                        
                    dataJSON["dnevenPromet_records"][len(dataJSON["dnevenPromet_records"])-1]["total_price"]=total_price
                        
                        
           
        with open('json/dnevenPromet.json','w') as outfile:
            json.dump(dataJSON,outfile)
            print(y)    