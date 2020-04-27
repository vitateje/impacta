fun main(args: Array<String>){
    var sobrenome: String
    sobrenome = "Tadeu"
    var nome = "Sousa" // se for na mesma linha nao precisa informar o tipo
    println("Olá $nome") // string template
    print(nome)
    print("tamanho da string:  ${nome.length}")
    val nao_muda = " Vitor Tadeu" // nao pode reatribuir valor
    var s:Any = "Vitor"
    println(s as? Int) // cast seguro se nao transformar, retorna null
    //print("${var.type}")
    
    //if (s is Int) {println("s é um inteiro")} 
    
}
