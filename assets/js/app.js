//var productR; za select ako imame vo js...
function postData(fileName,postJSON)
{		//console.log("bilee",postJSON );
		$.ajax({
			url:"../model/"+fileName,
			type:"post",
			contentType:"application/json; charset=utf-8",
			dataType:"json",
			data:JSON.stringify(postJSON),
			success:function(response){
				console.log("success");
			}

		});
	
	
}
/*function writeJSON(collection_name){
	var writeData=[{"collection_name":collection_name,"action":"create"}];
	postData(collection_name+".py",writeData);
}*/