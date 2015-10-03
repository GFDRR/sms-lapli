/**
 * Created by rpalexis on 10/1/15.
 */

$(document).ready(function(){
    $.get('/json_rap',function(data,status){
				//alert(data);
            //alert(data.table[0].dep)
        var i;
        var objs =data.table
        for(i=0;i<objs.length;i++){
            $('tbody').append("<tr><td>"+objs[i].dep+"</td><td>"+objs[i].com+"</td><td>"+objs[i].date+"</td><td>"+objs[i].moy+"</td></tr>")
        }
    });
});
