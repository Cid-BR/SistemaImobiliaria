function teste(){
  alert('Adriano');
}

function funcao_ajax(id_resposta, url_programa, valor_digitado) {
    //define object HttpResponse
    var reqHttp = null;
    
    if (window.XMLHttpRequest)
        reqHttp = new XMLHttpRequest();
    else if (window.ActiveXObject)
        reqHttp = new ActiveXObject("Microsoft.XMLHTTP");
    //end define object HttpResponse
    reqHttp.onreadystatechange = function() {
    
        if (reqHttp.readyState == 4) {
            if (reqHttp.status == 200) {
                id_resposta.innerHTML = reqHttp.responseText;
            } else {
                id_resposta.innerHTML = "(ERRO) " + reqHttp.status + "; " 
                + reqHttp.statusText
            }
        } 
        // else {
        //     id_resposta.innerHTML = "Aguardando...";
        // }
    }
    
    if (valor_digitado == '') 
        {
            reqHttp.open("GET", url_programa + "=" + 'all', true);
        }
        else{
            reqHttp.open("GET", url_programa + "=" + valor_digitado, true);           
        }
            
    reqHttp.send(null);
    
}

