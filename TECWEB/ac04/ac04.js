function soma(){
   var x = document.getElementById("a").value;
   var y = document.getElementById("b").value;
   var operacao = document.getElementById('operacao');
   if (operacao == '+')
      {var resultado = parseInt(x) + parseInt(y);
      alert(resultado);}
   
}