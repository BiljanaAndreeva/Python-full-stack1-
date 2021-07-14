w3.includeHTML();
w3.hide(".w3-green");/*
var vozilaObject=
    {"vozila_records":
       [
        {"ime_vozilo":"Renaut Megane 2" ,"broj_vozilo":42},
        {"ime_vozilo":"Wv Golf 4" ,"broj_vozilo":74},
		{"ime_vozilo":"audi " ,"broj_vozilo":33}	
        ]
	};


  w3.displayObject("id_vozila", vozilaObject); */
function writeJSON(collection_name){
		var writeData=[{"collection_name":collection_name,"action":"create"}];
		postData("vozila.py",writeData);
  }
w3.getHttpObject("../model/json/vozila.json",myVozila);

function myVozila(vozilaObject){
		w3.displayObject("id_vozila",vozilaObject);
}
  
function addVozila()
{
	var i_vozilo=document.getElementById("ime_vozilo").value;
	var br_vozilo=document.getElementById("broj_vozilo").value;
//	var vozilo_img=document.getElementById("vozilo_img").value;
	var vozilaObject=[
	{"ime_vozilo":i_vozilo ,"broj_vozilo":br_vozilo,"action":"insert"}];
	console.log(vozilaObject);
	postData("vozila.py",vozilaObject);
	w3.show(".w3-green");
}
function deleteVozila(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("vozila.py",deleteObject);
}
function editVozila(pk_value){
	
	var ime_vozilo=document.getElementById("ime_voz"+pk_value).value;
	var editObject=[
	{
	"ime_vozilo":ime_vozilo,
	"pk_value":pk_value,
	"action":"edit"
	}
	];
	console.log(editObject);
	postData("vozila.py",editObject);
}