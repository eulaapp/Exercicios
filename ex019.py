import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quinto aluno: ')

alunos = [aluno1, aluno2, aluno3,aluno4]

sorteio = random.choice(alunos)

print(f'O sorteado foi {sorteio}, parabéns!')