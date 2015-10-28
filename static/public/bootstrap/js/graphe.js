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
								data : [9,5,6,4,3]
							}
						]

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
