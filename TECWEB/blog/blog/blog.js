function novoTexto(estilo){
    var posts = document.getElementById("posts");
    var cor = document.getElementById("cor");
    var p = document.createElement("p");
    p.innerHTML = document.getElementById("texto").value;
    if(estilo == "n"){
        p.style.fontWeight = "bold";
    }
    if(estilo == "i"){
        p.style.fontStyle = "italic";
    }
    p.style.color = cor.value;
    posts.appendChild(p);
}
