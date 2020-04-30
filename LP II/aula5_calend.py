'''#implemente uma classe "calendario". essa classe
#devera receber em seu construtor 3 parametros:
#dia, mes, ano.
#um objeto da classe calendario devera implementar
#os seguintes metodos:
#amanha() - > muda a data do calendario pro dia seguinte
#semana_que_vem() -> muda a data do calendario para o mesmo dia 
#na proxima semana
#mes_que_vem() -> aumenta a data em 30 dias
#ano_que_vem() -> aumenta a data em um ano
#imprime_data() imprime a data interna do calendario no formato
#dd/mm/aaaa
#exemplo
#data = Calendario(14, 3, 2019)
#data.amanha()
#data.imprime_data -> 15/03/2019 '''



class Calendario():
    def __init__(self, dia_calend, mes_calend, ano_calend):
        self.dia = dia_calend
        self.mes = mes_calend
        self.ano = ano_calend


    def amanha_func(self):
            if hoje.dia == 30 and hoje.mes == 4 or hoje.mes == 6 or hoje.mes == 9 or hoje.mes == 11:
                self.amanha = 1
                self.amanha_mes = hoje.mes + 1
                self.amanha_ano = hoje.ano
            elif hoje.dia == 31 and hoje.mes == 1 or hoje.mes == 3 or hoje.mes == 5 or hoje.mes == 7 or hoje.mes == 8 or hoje.mes == 10:
                self.amanha = 1
                self.amanha_mes = hoje.mes + 1
                self.amanha_ano = hoje.ano
            elif hoje.dia == 28 and hoje.mes == 2:
                self.amanha = hoje.dia = 1
                self.amanha_mes = hoje.mes + 1
                self.amanha_ano = hoje.ano
            elif hoje.dia == 31 and hoje.mes == 12:
                self.amanha = 1
                self.amanha_mes = hoje.mes = 1
                self.amanha_ano = hoje.ano + 1
            else:
                self.amanha = hoje.dia + 1
                self.amanha_mes = hoje.mes
                self.amanha_ano = hoje.ano
                

    def semana_func(self):
        if hoje.dia <= 23 and hoje.mes == 4 or hoje.mes == 6 or hoje.mes == 9 or hoje.mes == 11:
            self.semana = hoje.dia + 7
            self.semana_mes = hoje.mes
        elif hoje.dia > 23 and hoje.mes == 4 or hoje.mes == 6 or hoje.mes == 9 or hoje.mes == 11:
            self.semana = (hoje.dia + 7) - 30
            self.semana_mes = hoje.mes + 1
        elif hoje.dia <= 24 and hoje.mes == 1 or hoje.mes == 3 or hoje.mes == 5 or hoje.mes == 7 or hoje.mes == 8 or hoje.mes == 10:
            self.semana = hoje.dia + 7
            self.semana_mes = hoje.mes
        elif hoje.dia > 24 and hoje.mes == 1 or hoje.mes == 3 or hoje.mes == 5 or hoje.mes == 7 or hoje.mes == 8 or hoje.mes == 10:
            self.semana = (hoje.dia + 7) - 31
            self.semana_mes = hoje.mes + 1



hoje = Calendario (25,4,2019)


print(hoje.dia,hoje.mes,hoje.ano)

hoje.amanha_func()
print(hoje.amanha,hoje.amanha_mes,hoje.amanha_ano)

hoje.semana_func()
print(hoje.semana,hoje.semana_mes)

#hoje.amanha_func()
#print(hoje.amanha,hoje.amanha_mes,hoje.amanha_ano)
#hoje.semana_func()
#print(hoje.semana)

#1 31 - 2 - 28 - 3 31 - 4 30 - 5 31 - 6 - 30 - 7 31 - 8 31 9 30 - 10 31 - 11 30 - 12 - 31
    #def final_mes(self):
     #   trinta=[4,6,9,11]
      #  trinta_1=[1,3,5,7,8,10,12]
       # vinte_oito=[2]
        #lista_mes = [trinta,trinta_1,vinte_oito]
       # self.lista_mes = lista_mes

#final_mes=final_mes()

#print(amanha())

    #def imprime_data_atual(self):
        #self.data_hoje(hoje)


    #def Amanha(self):
     #   self.dia_calend +=1
    
#data_hoje = imprime_data_atual()
#print(data_hoje)


    #def dia_hoje(self):
        #self.dia_hoje = 14 
        #self.mes_calend = 03
        #self.ano_calend = 2019

    #def dia_amanha(self):

#data = Calendario(14,3,2019)
#print(dia_calend)