ListaDatos = []
ListaDatos.push({categoria:"CAT 1",fecha:1433289600000,valor:50});
ListaDatos.push({categoria:"CAT 2",fecha:1433289600000,valor:80});
ListaDatos.push({categoria:"CAT 3",fecha:1433289600000,valor:90});
ListaDatos.push({fecha:1436054400000,categoria:"CAT 1",valor:10});
ListaDatos.push({fecha:1436054400000,categoria:"CAT 2",valor:10});
ListaDatos.push({fecha:1436054400000,categoria:"CAT 3",valor:10});
ListaDatos.push({categoria:"CAT 1",fecha:1436832000000,valor:70});
ListaDatos.push({categoria:"CAT 2",fecha:1436832000000,valor:70});
ListaDatos.push({categoria:"CAT 3",fecha:1436832000000,valor:30});


dadesnoves = [];
dadesnoves.push({categoria:"CAT 2",fecha:1433289600000,valor:1});
dadesnoves.push({categoria:"CAT 2",fecha:1433289600000,valor:1});
dadesnoves.push({categoria:"CAT 2",fecha:1433289600000,valor:1});
dadesnoves.push({fecha:1436054400000,categoria:"CAT 1",valor:10});
dadesnoves.push({fecha:1436054400000,categoria:"CAT 1",valor:10});
dadesnoves.push({fecha:1436054400000,categoria:"CAT 1",valor:10});
dadesnoves.push({fecha:1436054400000,categoria:"CAT 1",valor:10});

var arr = ListaDatos; // Unirà ListaDatos + dadesnoves


for (var elobj in dadesnoves) {
	existe=0;
	arr.map(function(elobjeto) {(elobjeto.categoria === dadesnoves[elobj].categoria) && (elobjeto.fecha === dadesnoves[elobj].fecha) && (existe = elobjeto.valor);});
	if (existe) {
		// Si existeix actualitzo el valor suman el nou al que ja està
		eltotal=existe+dadesnoves[elobj].valor;
		arr.map(function(elobjeto) {(elobjeto.categoria === dadesnoves[elobj].categoria) && (elobjeto.fecha === dadesnoves[elobj].fecha) && (elobjeto.valor=eltotal)});
	} else {
		arr.push({categoria:dadesnoves[elobj].categoria,fecha:dadesnoves[elobj].fecha,valor:dadesnoves[elobj].valor});
		//{categoria:elobj.categoria,fecha:elobj.fecha,valor:elobj.valor}
	}
}


document.write("<pre>ELOBJ<br />" + JSON.stringify(arr,null,2) + "<br /> Longitud: " + arr.length + "</pre>");


	// FI PINTAR DADES //

	// TEST CERCA AMB GREP //

	datosOrdenados3="";
	trobatsCat = $.grep(ListaDatos, function(ListaDatos){return ListaDatos.categoria === 'CAT 1';});
	datosOrdenados3=datosOrdenados3+'<br /><br />Trobats CAT == CAT 1:<br />' + JSON.stringify(trobatsCat);

	trobatsData = $.grep(trobatsCat, function(trobatsCat){return trobatsCat.fecha === 1435795200000;});

	datosOrdenados3=datosOrdenados3+'<br /><br />Registres (fecha === 1435795200000 && CAT === CAT 1):<br />' + JSON.stringify(trobatsData);
	datosOrdenados3=datosOrdenados3+'<br /><br />DATA valor (fecha === 1435795200000 && CAT === CAT 1):<br />' + trobatsData[0].valor;
	// FI CERCA AMB GREP //

