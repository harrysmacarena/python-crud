var mpComuna = new FrComuna();
function FrComuna(){
	this.loadCombo = function(stIdProvincia){
		var stDatos = "idProvincia=" + stIdProvincia
		ventana.getPostHtml("selComuna","comunaCombo/",stDatos)		
	}
	
	this.edit= function(pCodigo){
		var stData = "codigo=" + pCodigo
		ventana.getPostHtml('containerRight','comunaFrm/',stData)
	}
	this.leer= function(){
		var stData = "codigo=" + document.getElementById("txCodigo").value;
		var objComuna = ventana.getPostData("comunaLeer",stData)
		if (objComuna.length ==0){
		    document.getElementById("btEliminar").disabled = true;	
		    document.getElementById("btActualizar").innerText = "Crear";
		}
		else {
			document.getElementById("txDescrip").value 
			         = objComuna[0].fields.nombre_comuna;
			document.getElementById("txImagen").value 
			         = objComuna[0].fields.stImagen;
			document.getElementById("btEliminar").disabled = false;
			document.getElementById("btActualizar").innerText = "Actualizar";
		}
		document.getElementById("btLeer").disabled = true;
		document.getElementById("btActualizar").disabled = false;
		document.getElementById("btCancelar").disabled = false;
        document.getElementById("txCodigo").disabled = true;
		document.getElementById("txDescrip").disabled = false;
		document.getElementById("txImagen").disabled = false;
		document.getElementById("cbRegion").disabled = false;
		document.getElementById("cbProvincia").disabled = false;
	}
	this.actualizar= function(){
		var stData = "codigo=" + document.getElementById("txCodigo").value
		       + "&descrip=" + document.getElementById("txDescrip").value
		       + "&imagen=" + document.getElementById("txImagen").value
			       ;
	    var objComuna = ventana.getPostData("comunaSave",stData)
	    if (objComuna.ok){
		   alert(objComuna.msg)
		   mpComuna.cancelar()
		   return
		}
		alert("Error al Actualizar " + objComuna.msg)
	}
	this.eliminar= function(){
		var stData = "codigo=" + document.getElementById("txCodigo").value
			       ;
	    var objComuna = ventana.getPostData("comunaDelete",stData)
	    if (objComuna.ok){
		   alert(objComuna.msg)
		   mpComuna.cancelar()
		   return
		}
		alert("Error al Actualizar" + objComuna.msg)
	}
	this.listar= function(){
		javascript:ventana.showHTML('containerRight','comunaListado')
	}			
	this.cancelar= function(){
		document.getElementById("btLeer").disabled = false;
		document.getElementById("btActualizar").disabled = true;
		document.getElementById("btEliminar").disabled = true;
		document.getElementById("btCancelar").disabled = true;
        document.getElementById("txCodigo").disabled = false;
		document.getElementById("txDescrip").disabled = true;
		document.getElementById("txImagen").disabled = true;
		document.getElementById("cbRegion").disabled = true;
		document.getElementById("cbProvincia").disabled = true;
        document.getElementById("txCodigo").value=""
		document.getElementById("txDescrip").value=""
		document.getElementById("txImagen").value=""
	}			
	this.provinciaRegion=function(stIdRegion){
		//alert(stIdRegion)
		var stData = "idRegion=" + stIdRegion
		ventana.getPostHtml('cbComuna','provinciaFrm/',stData)
	}

}