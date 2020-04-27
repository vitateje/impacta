'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 1                                  ║
║ Turma         :  1B (noturno)                                                ║
║ Professor     :  Lucio Nunes de Lira                                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  Exercícios Resolvidos (Estrutura de seleção)                ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

# --------------------------------------
# Exercício 5a (1ª forma)
# --------------------------------------

num = float(input('Valor: '))
if 1 <= num <= 100:
    print('dentro do intervalo')

# --------------------------------------
# Exercício 5a (2ª forma)
# --------------------------------------

num = float(input('Valor: '))
if 1 <= num and num <= 100:
    print('dentro do intervalo')

# --------------------------------------
# Exercício 5b (1ª forma)
# --------------------------------------

num = float(input('Valor: '))
if 30 < num < 70:
    print('dentro do intervalo')
else:
    print('fora do intervalo')

# --------------------------------------
# Exercício 5b (2ª forma)
# --------------------------------------

num = float(input('Valor: '))
if 30 < num and num < 70:
    print('dentro do intervalo')
else:
    print('fora do intervalo')

# --------------------------------------
# Exercício 6.2
# --------------------------------------

n = int(input('Qual número? '))
if n % 2 == 0:
    print('par')
else:
    print('ímpar')

# --------------------------------------
# Exercício 6.3
# --------------------------------------

compra = float(input('Valor de compra: '))
if compra < 20:
    venda = compra * 1.45
else:
    venda = compra * 1.30
print('Valor de venda: R$ %.2f' % venda)
