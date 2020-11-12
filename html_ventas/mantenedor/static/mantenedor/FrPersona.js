//alert("persona")
mpPersona = new FrPersona();
function FrPersona(){
	//alert("persona new")
	function leerLocal(){
		alert("Leyendo Local")

	}
	this.edit = function (stRun){
		//alert("Editando " + stRun)
		var stDatos = "run=" + stRun
		var reg = ventana.getPostHtml("containerRight","personaFrm/",stDatos)
	}
	this.leer = function(){
		var stDatos = "runHarrys=" + document.getElementById("txRun").value
		var reg = ventana.getPostData("personaLeer",stDatos)

		if (reg.length ==0){
		    document.getElementById("btEliminar").disabled = true;	
		    document.getElementById("btActualizar").innerText = "Crear";
		}
		else {
			document.getElementById("txNombres").value=reg[0].fields.nombres;     
			document.getElementById("txApePaterno").value=reg[0].fields.apePaterno;     
			document.getElementById("txApeMaterno").value=reg[0].fields.apeMaterno;   
			document.getElementById("txImagen").value=reg[0].fields.imagen; 
			document.getElementById("btEliminar").disabled = false;
			document.getElementById("btActualizar").innerText = "Actualizar";
		}
		
		document.getElementById("btLeer").disabled = true;
		document.getElementById("btActualizar").disabled = false;
		document.getElementById("btCancelar").disabled = false;

        document.getElementById("txRun").disabled = true;
		document.getElementById("txNombres").disabled = false;
		document.getElementById("txApePaterno").disabled = false;		 
		document.getElementById("txApeMaterno").disabled = false;		 
		document.getElementById("txImagen").disabled = false;		 

		document.getElementById("cbRegion").disabled = false;		 
		document.getElementById("cbProvincia").disabled = false;		 
		document.getElementById("cbComuna").disabled = false;		 

		/*
		alert("Leyenco Publica OK" + reg.ok)
		alert("Leyenco Publica msg" + reg.msg)
		alert("Leyenco Publica claudio" + reg.claudio)
		*/
		//leerLocal()
	}
	this.actualizar = function(){
		//alert(2)
		var stDatos = "run=" + document.getElementById("txRun").value
		       + "&nombres=" + document.getElementById("txNombres").value
		       + "&apePaterno=" + document.getElementById("txApePaterno").value		
		       + "&apeMaterno=" + document.getElementById("txApeMaterno").value		
		       + "&imagen=" + document.getElementById("txImagen").value		
		       + "&cbComuna=" + document.getElementById("cbComuna").value
		       ;

        alert(stDatos)		       
		var reg = ventana.getPostData("personaActualizar",stDatos)
		if (reg.ok){
			alert(reg.msg)
			return
		}
		alert("Error ,"+ reg.msg)
		//alert("Actuaizar Publica")
	}
	this.eliminar = function(){
		var stDatos = "run=" + document.getElementById("txRun").value
		var reg = ventana.getPostData("personaDelete",stDatos)
		if (reg.ok){
			alert(reg.msg)
			return
		}
		alert("Error ,"+ reg.msg)

		//alert("eliminar Publica")
	}
	this.cancelar = function(){
		//alert("Cancelar Publica")
		document.getElementById("btLeer").disabled = false;
		document.getElementById("btActualizar").disabled = true;
		document.getElementById("btEliminar").disabled = true;
		document.getElementById("btCancelar").disabled = true;

        document.getElementById("txRun").disabled = false;
		document.getElementById("txNombres").disabled = true;
		document.getElementById("txApePaterno").disabled = true;		 
		document.getElementById("txApeMaterno").disabled = true;		 
		document.getElementById("txImagen").disabled = true;		

        document.getElementById("txRun").value = ""
		document.getElementById("txNombres").value = ""
		document.getElementById("txApePaterno").value = ""
		document.getElementById("txApeMaterno").value = ""
		document.getElementById("txImagen").value = ""

		document.getElementById("cbRegion").disabled = true;		 
		document.getElementById("cbProvincia").disabled = true;		 
		document.getElementById("cbComuna").disabled = true;		 


	}
	this.listar = function(){
		ventana.showHTML('containerRight','personaListado')
	}				
}