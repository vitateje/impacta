from aula9 import Televisao

tv_quarto = Televisao('Samsung', 34)
try:
    tv_quarto.set_tamanho('-5.5')
except ValueError as err: # except exception pega todos os erros
    print(err)
except TypeError: # except fala o que fazer caso aconteça o erro
    print('O tipo esta errado')
except Exception:
    print('outros erros')
else: # caso nao de erro executa a func do else
    print('nao deu erro')
