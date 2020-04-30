class Calendario():
    def __init__(self, dia_calend, mes_calend, ano_calend):
        self.dia = dia_calend
        self.mes = mes_calend
        self.ano = ano_calend
        self.meses = {1: 31, 2: 28, 3: 31, 4: 30,
                      5:31, 6:30, 7:31, 8:31,
                     9:30, 10:31, 11:30, 12 :31}

    def imprime_data(self):
        print(f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}') # documentação de f strings - formatação

    def amanha(self):
       
        if self.dia < self.meses [self.mes]:
            self.dia += 1
        else:
            
            if self.mes == 12:
                self.dia = 1
                self.mes = 1
                self.ano += 1
            else:

            


data = Calendario(21, 3, 2019)

data.imprime_data()
