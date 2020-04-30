function mostrarAtivo(tag){
  var tag_li = document.getElementById('lista_menu');
  var tag_a = tag_li.getElementsByTagName('a');
  for (i=0; i<tag_a.length; i++ ){
    tag_a[i].style.backgroundColor = "";
    tag_a[i].style.color = "";
  }
  tag.style.backgroundColor = "#ff0000"; // altera o fundo
  tag.style.color = "#ffffff"; // altera a cor
}

function mostrarAtivo2(tag){
  var tag_li = document.getElementsById('menu');
  var tag_a = tag_li.getElementsByTagName('a');
  for (i=0; i<tag_a.length; i++ ){
    tag_a[i].style.backgroundColor = "";
    tag_a[i].style.color = "";
  }
  tag.style.backgroundColor = "#ff0000"; // altera o fundo
  tag.style.color = "#ffffff"; // altera a cor
}