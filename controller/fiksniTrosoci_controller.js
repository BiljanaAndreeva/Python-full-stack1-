function writeJSON(collection_name){
	var writeData=[{"collection_name":collection_name,"action":"create"}];
	postData("fiksniTrosoci.py",writeData);
}
w3.getHttpObject("../model/json/fiksniTrosoci.json",myFixTrosok);

function myFixTrosok(fixObject){
		w3.displayObject("id_fiksniTrosoci",fixObject);
	
}

function addFixTrosoci(){
	var kirija=document.getElementById("kirija").value;
	var smetkovoditel=document.getElementById("smetkovoditel").value;
	var banka=document.getElementById("banka").value;
	var komunikaciski_uslugi=document.getElementById("komUslugi").value;
	var drug_trosokF=document.getElementById("drug_trosokF").value;
	var cenaF=document.getElementById("cenaF").value;
	var fixObject=[
	{"kirija":kirija,
	"smetkovoditel":smetkovoditel,
	"banka":banka,
	"komunikaciski_uslugi":komunikaciski_uslugi,
	"drug_trosokF":drug_trosokF,
	"cenaF":cenaF,
	"data":[],
	"action":"insert"}];
	console.log(fixObject);
	postData("fiksniTrosoci.py",fixObject);
}

function deleteFiksniTrosoci(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("fiksniTrosoci.py",deleteObject);
}	 
/*$("#addArticle").click(function(){
	$("#id_dop_trosok").clone().appendTo("table");
	
	console.log("klik");
})
	 */