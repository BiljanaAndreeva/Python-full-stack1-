w3.hide('#t_p');

var invoiceDetails;
w3.includeHTML();
function writeJSON(collection_name){
	var writeData=[{"collection_name":collection_name,"action":"create"}];
	postData("dnevenPromet.py",writeData);
}
w3.getHttpObject("../model/json/dnevenPromet.json",myDnevenPromet);


function myDnevenPromet(dnevenPrometObject){
		invoiceDetails=dnevenPrometObject;
	    productR=dnevenPrometObject; 
		w3.displayObject("id_dnevenPromet",dnevenPrometObject);
	
}
w3.getHttpObject("../model/json/dnevenPromet.json",myDnevenPromet1);


function myDnevenPromet1(dnevenPrometObject1){
	    productR=dnevenPrometObject1;
		w3.displayObject("id_dnevenPromet1",dnevenPrometObject1);
	
}
function dnevenPromet(){
	var numItems=$('tbody>#id_dop_trosok').length;
	var vraboteni=document.getElementById("id_vraboteni").value;
	var vozila=document.getElementById("id_vozila").value;
	var pocetni_km=document.getElementById("poc_km").value;
	var krajni_km=document.getElementById("kraj_km").value;
	var prazni_km=document.getElementById("praz_km").value;
	var dnevenPrometObject=[
	{"vraboteni":vraboteni,"vozila":vozila,
	"pocetni_km":pocetni_km ,
	"krajni_km":krajni_km,
	"prazni_km":prazni_km,
	"action":"insert",
	"data_promet":"",
	"dopolnitelen_trosok":[
	/*{
		"opis":document.getElementById("id_opis0").value,
		"cena":document.getElementById("id_cena0").value
	}*/
	]
	}];
	console.log("broj"+numItems);
	$("tbody>#id_dop_trosok").each(function(index){
		    
			
			 dnevenPrometObject[0]["dopolnitelen_trosok"].push({
		    "opis":document.getElementById("id_opis"+index).value,
			"cena":document.getElementById("id_cena"+index).value
			
	   });
    });		
	console.log(dnevenPrometObject);
	postData("dnevenPromet.py",dnevenPrometObject);
}

function deleteDnevenPromet(pk_value){
	var deleteObject=[{"pk_value":pk_value,"action":"delete"}];
	console.log(deleteObject);
	postData("dnevenPromet.py",deleteObject);
}	 

function editDnevenPromet(pk_value){
	
	var pocetni_km=document.getElementById("poc_km_"+pk_value).value;
	var krajni_km=document.getElementById("kraj_km_"+pk_value).value;
	var prazni_km=document.getElementById("praz_km_"+pk_value).value;
	var editObject=[
	{
	"pocetni_km":pocetni_km ,
	"krajni_km":krajni_km,
	"prazni_km":prazni_km,
	"pk_value":pk_value,
	"action":"edit"
	}
	];
	console.log(editObject);
	postData("dnevenPromet.py",editObject);
}
$("#addArticle").click(function(){
	var numItems=$('tbody>#id_dop_trosok').length;
	//console.log(numItems);
	$("#t_p").append('<tr id="id_dop_trosok" product="'+numItems+'">\
			    <th>opis\
			   <input type="text" id="id_opis'+numItems+'" name="id_opis">\
			   </th>\
			   <th>cena\
			   <input type="text" id="id_cena'+numItems+'" name="id_cena"> \
			   </th>\
			</tr>');
	console.log(productR["dnevenPromet_records"]);
})
function showDetails(getID){
		console.log(invoiceDetails);
		var drawDetails='';
		for(var i=0;i<invoiceDetails.dnevenPromet_records.length;i++){
			if(getID==invoiceDetails.dnevenPromet_records[i]._id){
				//telo if
				var productList=invoiceDetails.dnevenPromet_records[i].dopolnitelen_trosok;
				//console.log(invoiceDetails.dnevenPromet_records[i].dopolnitelen_trosok);

				for(var j=0;j<productList.length;j++){
				drawDetails+='<li>'+productList[j].opis+" "+productList[j].cena
				+'</li>';
				}//for za detali na proizvodi
			}//sporedba if getID
			
		}
    $("ul#listProducts").append(drawDetails);		
		
	w3.show('#details_invoice');	
}
	 