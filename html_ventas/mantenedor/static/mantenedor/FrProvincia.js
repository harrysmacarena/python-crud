mpProvincia = new FrProvincia();
function FrProvincia(){
	this.loadCombo = function(stIdRegion){
		//alert(stIdRegion)
		var stDatos = "idRegion=" + stIdRegion
		ventana.getPostHtml("selProvincia","provinciaCombo/",stDatos)		
	}
}	
