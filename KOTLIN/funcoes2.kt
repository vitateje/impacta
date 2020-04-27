fun toList(vararg args:String): List<String>{
    var list = ArrayList<String>() // tipo especial de lista
    for (e in args){ // loop for
        list.add(e) // == append do python (adicionando cada item na lista)
    }
    return list
} // pode receber n strings n parametros

fun <T> toList2(vararg args:T): List<T>{ // T para itens genericos
    var list = ArrayList<T>() // tipo especial de lista
    for (e in args){ // loop for
        list.add(e) // == append do python (adicionando cada item na lista)
    }
    return list
} // pode receber n strings n parametros


fun main(args: Array<String>){
  println(toList("1","2","2"))
  println(toList2(1,"Vitor",6))
}