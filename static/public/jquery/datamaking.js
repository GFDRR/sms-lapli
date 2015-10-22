/**
 * Created by rpalexis on 10/1/15.
 */

$(document).ready(function(){
    $.get('/rapport/json_rap',function(data,status){
				//alert(data);
            //alert(data.table[0].dep)
            //alert("Je suis")
        var i;
        var objs =data.table
        for(i=0;i<objs.length;i++){
            $('tbody').append("<tr><td>"+objs[i].dep+"</td><td>"+objs[i].com+"</td><td>"+objs[i].date+"</td><td>!"+objs[i].nbr+"!</td><td>"+objs[i].moy+"</td></tr>")
        }
    });
});

/*
* Assure le changement de blocs dans la partie publique
* */

$(document).ready(function(){
    $('.nav-sidebar #overview, .dropdown-menu li').click(function(e){
        e.preventDefault()
        //alert("On m'a clique!!");
        var sltedId=$(this).children("a").attr("href");
        alert(sltedId);
        $('.nav-sidebar li').removeAttr("class");//supprime les active
        $(this).attr("class","active");//ajoute les active au li selectionne
        //selection de tous les blocs ayant les articles
       $("#lesblocs").children('[class*="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main"]').attr("class","col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main hidenSubMenuContent");
        //affichage du block selectionnes
        $("#lesblocs "+sltedId).attr("class","col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main showSubMenuContent");
    });
});