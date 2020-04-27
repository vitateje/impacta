fun parOuImpar(a: Int): String {
    return if (a%2 == 0) "o numero $a é par" else "impar"
} // definir o tipo do parametro de entrada e caso tenha a função tenha retorno determinar o tipo de saida, nesse caso havera uma entrada int e uma saida str

fun parOuImpar2(a:Int) = if (a%2==0) "par" else "impar" // lambda

fun enviaEmail(usuario: String, titulo: String? = null): String {
    //val s = if (titulo != null) titulo else "bem vindo"
    val s = titulo?: "Bem Vindo" // ? avalia se é nulo e se for valor padrao
    return "$s $usuario"
} // ? caso nao seja Str retorna null e define um valor padrao


fun main(args: Array<String>){
    println(parOuImpar(1)) // chamando função
    println(parOuImpar2(2))
    
    println(enviaEmail(titulo="Olá", usuario="Fernando")) // parametros nomeados
    println(enviaEmail("Fernando"))
}

// Unit = None = Void (nao tem retorno na funcao)