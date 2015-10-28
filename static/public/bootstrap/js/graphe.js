$(document).ready(function(){
    $.get('/rapport/average',function(data,status){
				// alert(data);
            //alert(data.table[0].dep);
        var i;
        var objs = data.table

		labl =[]
		datasz = []

		for(i=0;i<objs.length;i++){
            labl.push(objs[i].dep)
			datasz.push(objs[i].moy)
        }
		var lineChartData = {
			labels : labl,
			datasets : [
				{
					label: "My Second dataset",
					fillColor : "rgba(101,178,200,0.2)",
					strokeColor : "rgba(101,178,200,1)",
					pointColor : "rgba(101,178,200,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(101,178,200,1)",
					data : datasz
				}
			]

		}
		var ctx = $("#canvas").get(0).getContext("2d");
		var myNewChart = new Chart(ctx).Bar(lineChartData, {
			bezierCurve: true
		});

    });

	//Gestion de la comparaison entre les departements
	$(".dropdown-menu li a").click(function(){
			if ($(this).attr("href") == "#rap1"){
				$.get('/rapport/pluviometrie/comp/',function(data,status){
							 //alert(data.jr);
						//alert(data.table[0].dep);
					var i;
					var objs = data.table
                    //alert(data.table[0].nomDep)
                    //les coulleurs
                    fill = ["rgba(124,232,128,0.5)","rgba(4,11,95,0.5)","rgba(34,177,18,0.5)","rgba(140,171,17,0.5)","rgba(124,232,128,0.5)","rgba(4,39,28,0.5)"]
                    stroke = ["rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)","rgba(4,39,28,0.5)"]
                    //les coulleurs

					datasz = []

					for(i=0;i<objs.length;i++){
						datasz.push({
                                label: "Graph for "+objs[i].nomDep,
								fillColor : fill[i],
								strokeColor : stroke[i],
								pointColor : "rgba(101,178,200,1)",
								pointStrokeColor : "#fff",
								pointHighlightFill : "#fff",
								pointHighlightStroke : "rgba(101,178,200,1)",
								data :objs[i].moyDep
                        })
					}

					var lineChartData = {
						labels : data.jr,
						datasets : datasz
					}
					var ctx = $("#canvas2").get(0).getContext("2d");
					var myNewChart = new Chart(ctx).Line(lineChartData, {
						bezierCurve: true
					});

				});
			}
	})
	});

//Gestion de comparaison
$(document).ready(function(){
	$(".selectpicker").click(function(){
		alert("Moi Alexis")
	})
});
