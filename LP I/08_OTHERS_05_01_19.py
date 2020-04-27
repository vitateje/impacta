print('... ## OTHERS 2019 ## ...')

nome=input('Digite Seu Nome: ')
print('Olá querido, ',nome)

def func1 ():
    while True:
        lucknumber=input('Digite seu numero da sorte: ')
        message='what a number!'
        if lucknumber=='1' or lucknumber=='2':
            print(message)
        repetir=input('Deseja Repetir? ')
        if repetir != 'sim' and repetir != 'SIM': break
    return 'FIM!'
x=func1()
print(x)

#exercicios
def func5 ():
    produto=float(input('Digite o valor do produto '))
    desconto=(produto*0.9)
    print('O valor com desconto fica R$', desconto)

chama=func5()
