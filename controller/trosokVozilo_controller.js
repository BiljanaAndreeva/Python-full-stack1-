w3.includeHTML();
function writeJSON(collection_name){
		var writeData=[{"collection_name":collection_name,"action":"create"}];
		postData("trosokVozilo.py",writeData);
}
w3.getHttpObject("../model/json/trosokVozilo.json",MyTrosokVozilo);

function MyTrosokVozilo(TvObject){
		w3.displayObject("id_trosokVozilo",TvObject);
	
}
  
function addTrosokVozilo(){
	var vozila=document.getElementById("id_vozila").value;
	var gorivo=document.getElementById("gorivo").value;
	var drug_trosok=document.getElementById("drugTrosok").value;
	var cena=document.getElementById("cenaT").value;
	var TvObject=[
	 {"vozila":vozila,
	 "gorivo":gorivo,
	 "drug_trosok":drug_trosok,
	 "cena":cena,
	 "action":"insert",
	 "data":"" 
	 }];
	 console.log(TvObject);
	  postData("trosokVozilo.py",TvObject);
}
function deleteTrosokVozilo(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("trosokVozilo.py",deleteObject);
}