'''═════════════════════════════════════════════════════════════════════════════
 Instituição  : Faculdade Impacta Tecnologia
 Curso        : Análise e Desenvolvimento de Sistemas
 Disciplina   : Linguagem de Programação 1
 Turma        : 1B (noite)
 Professor    : Lucio Nunes de Lira
════════════════════════════════════════════════════════════════════════════════
 Programa     : Exemplos de uso do operador IN. 
═════════════════════════════════════════════════════════════════════════════'''

'''─────────────────────────────────────────────────────────────────────────────
Verificar se um valor está em uma sequência de valores.
─────────────────────────────────────────────────────────────────────────────'''
# 1º Exemplo

valor = 10
sequencia = [30,40,20,10,50]
if valor in sequencia:
    print('encontrei!')
else:
    print('não encontrei')

# 2º Exemplo

valor = 10
if valor in [30,40,20,10,50]:
    print('encontrei!')
else:
    print('não encontrei')

# 3º Exemplo

valor = 'u'
if valor in 'abcdefghijklmnopqrstuvwxyz':
    print('é uma letra minúscula!')
else:
    print('não é uma letra minúscula')

# 4º Exemplo

if 7.5 in (6.9, 'legal', 7.5, True):
    print('encontrei minha nota!')
else:
    print('que pena, não achei')

# 5º Exemplo

if 'mãe' in ['pai', 'irmão', 'irmã', 'mãe', 'avó']:
    print('encontrei minha mãe!')
else:
    print('não achei minha mãe')

'''─────────────────────────────────────────────────────────────────────────────
Verificar se um valor NÃO está em uma sequência de valores.
─────────────────────────────────────────────────────────────────────────────'''
# 1º Exemplo

valor = 100
sequencia = [30,40,20,10,50]
if valor not in sequencia:
    print('não está na sequência')
else:
    print('está na sequência')

# 2º Exemplo

valor = 100
if valor not in [30,40,20,10,50]:
    print('não está na sequência')
else:
    print('está na sequência')

# 3º Exemplo

valor = 'U'
if valor not in 'abcdefghijklmnopqrstuvwxyz':
    print('não é uma letra minúscula')
else:
    print('é uma letra minúscula')

# 4º Exemplo

if 7.5 not in (6.9, 'legal', 7.5, True):
    print('não encontrei minha nota')
else:
    print('encontrei minha nota')

# 5º Exemplo

if 'namorada' not in ['pai', 'irmão', 'irmã', 'mãe', 'avó']:
    print('não encontrei minha namorada')
else:
    print('encontrei minha namorada')
