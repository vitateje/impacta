function validaCadastroAluno(){
    var nome = document.forms["cadastroAluno"]["nome"].value; /*name do form & id.value */
    var nota = document.forms["cadastroAluno"]["nota"].value;
    if(nome == "" || nota == ''){
        alert("Favor preencher o nome!");
        return false;

    }
    return true;
}