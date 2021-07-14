
w3.hide('#novVraboten');
w3.includeHTML();
//function isAdult(age)
//{

//alert("jas imam "+age);
//if(age>=18)
//{
//alert("Vie ste polnoleten");
//console.log("Vie ste polnoleten");
//}
//else
//{
//alert("Vie ste maloleten");
//console.log("Vie ste maloleten");
//}
//}//end isAdult


/*var vraboteniObject=
    {"vraboteni_records":

       [
        {"ime":"Zoran" ,"prezime":"Kekovski"},
        {"ime":"Vlade" ,"prezime":"Georgievski"},
		{"ime":"Boce","prezime":"Veljanovski"}
		]
	};

w3.displayObject("id_vraboteni", vraboteniObject);
 
function addVraboteni()

{
	
	var ime_vraboten=document.getElementById("ime").value;
	var prezime_vraboten=document.getElementById("prezime").value;
	var vraboteniObject=[
	{"ime":ime_vraboten ,"prezime":prezime_vraboten}];
	console.log(vraboteniObject);
	
}*/
function writeJSON(collection_name){
		var writeData=[{"collection_name":collection_name,"action":"create"}];
		postData("vraboteni.py",writeData);
}
w3.getHttpObject("../model/json/vraboteni.json",myVraboteni);

function myVraboteni(vraboteniObject){
		w3.displayObject("id_vraboteni",vraboteniObject);
	
}
  /*var myObject=
 {
	 "vraboteni_records":
	 [
	 {"ime":"Zoran","prezime":"Kekovski"},
	{ "ime":"Boce","prezime":"Veljanovski"},
		{"ime":"Vlade","prezime":"Georgievski"}
		 
	 ]
 };

 w3.displayObject("id_vraboteni", myObject);*/	 
function addVraboteni(){
	var ime_vraboten=document.getElementById("ime_vraboten").value;
	var prezime_vraboten=document.getElementById("prezime_vraboten").value;
	var vraboteniObject=[
	 {"ime":ime_vraboten,"prezime":prezime_vraboten,"action":"insert"}];
	 console.log(vraboteniObject);
	  postData("vraboteni.py",vraboteniObject);
}
function deleteVraboteni(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("vraboteni.py",deleteObject);
}
function editVraboteni(pk_value){
	
	var prezime=document.getElementById("prezime_vraboten_"+pk_value).value;
	
	var editObject=[
	{
	"prezime":prezime,
	"pk_value":pk_value,
	"action":"edit"
	}
	];
	console.log(editObject);
	postData("vraboteni.py",editObject);
}