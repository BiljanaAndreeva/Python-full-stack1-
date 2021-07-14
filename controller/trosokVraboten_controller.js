
w3.hide('#novVraboten');
w3.includeHTML();
function writeJSON(collection_name){
		var writeData=[{"collection_name":collection_name,"action":"create"}];
		postData("trosokVraboten.py",writeData);
}
w3.getHttpObject("../model/json/trosokVraboten.json",myTrosokVraboten);

function myTrosokVraboten(trosokVrabotenObject){
		w3.displayObject("id_trosokVraboten",trosokVrabotenObject);
	
}
  
function addTrosokVraboten(){
	var vraboteni=document.getElementById("id_vraboteni").value;
	var plata=document.getElementById("plata_vraboten").value;
	var pridonesi=document.getElementById("pridonesi_vraboten").value;
	var drug_Trosok=document.getElementById("drug_t").value;
	var Cena=document.getElementById("cena_dt").value;
	var trosokVrabotenObject=[
	 {"vraboteni":vraboteni,"plata":plata,"pridonesi":pridonesi,"drug_Trosok":drug_Trosok,"Cena":Cena,"action":"insert"}];
	 console.log(trosokVrabotenObject);
	  postData("trosokVraboten.py",trosokVrabotenObject);
}
function deleteTrosokVraboten(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("trosokVraboten.py",deleteObject);
}
function editTrosokVraboten(pk_value){
	
	var drug_Trosok=document.getElementById("drug_t"+pk_value).value;
	
	var editObject=[
	{
	"drug_Trosok":drug_Trosok,
	"pk_value":pk_value,
	"action":"edit"
	}
	];
	console.log(editObject);
	postData("trosokVraboten.py",editObject);
}