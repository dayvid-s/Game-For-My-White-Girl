import time
import random
import emoji

# para baixar modulos, faça py -m pip install    packagename
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print()
print('                                           \033[1;34m-BEM VINDOS, E QUE COMECE A JECKAGEM!-\033[m')

time.sleep(2)

print()

print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('             \033[1;31m[REGRAS DO JOGO]\n\033[m'
      '1° Regra: Não pode arregar do seu desafio.\n'
      '\n'
      '2° Regra: Só existe a primeira regra. (STONKS)')

print()

print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)

challenges = ['tirar uma peça de roupa do parceiro (A).',
              'fazer a trend do tiktok.',
              'se beijar com mão boba.',
              'deixar o parceiro(A) fazer o que quiser com você por 5 minutos.',
              'beijar no mamilo do parceiro (A).']

Nchallenges = 0  # Numero de desafios
Cchallenges = 1  # contador de desafios
random.shuffle(challenges)

while Cchallenges <= 5:
    print()
    choice = str(input(f'Está pronto(A) para o {Cchallenges}° desafio?')).upper().strip()
    print()
    while choice not in 'SIM':
        choice = str(input('Você só tem a opção de dizer sim, então... ')).upper().strip()
        print()
    print(f'O seu desafio é {challenges[Nchallenges]} ')
    Nchallenges += 1
    time.sleep(5)
    Cchallenges += 1

print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print()
print('                                           \033[1;40mPARABÉNS, VOCÊS CHEGARAM '
      'NO NIVEL MÉDIO.!\033[m')
print('                                           \033[1;40mCONTINUEM, O JOGO ESTÁ '
      'APENAS COMEÇANDO\033[m', end='')

time.sleep(5)
print(emoji.emojize('\033[1;40m :smirk:\033[m', use_aliases=True), end='')
print(emoji.emojize('\033[1;40m:smirk:\033[m', use_aliases=True))

print()

print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)
print('\033[1;35m===\033[m' * 40)

challenges = ['desafio 6.',
              'desafio7.',
              'desafio8.',
              'desafio9.',
              'desafio10.']

Nchallenges = 0  # Numero de desafios
Cchallenges = 6  # contador de desafios
random.shuffle(challenges)

while Cchallenges <= 10:
    print()
    choice = str(input(f'Está pronto(A) para o {Cchallenges}° desafio?')).upper().strip()
    print()
    while choice not in 'SIM':
        choice = str(input('Você só tem a opção de dizer sim, então... ')).upper().strip()
    print(f'O seu desafio é {challenges[Nchallenges]} ')
    Nchallenges += 1
    time.sleep(5)
    Cchallenges += 1

print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print()
print('                                     \033[1;40mPARABÉNS, VOCÊS CHEGARAM NO'
      ' NIVEL INTERMÉDIARIO.!\033[m')
print('                                               \033[1;40mA PARADA TÁ TENS'
      'A, MINHA AMIGOS\033[m')

print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print()

challenges = ['desafio 11.',
              'desafio12.',
              'desafio13.',
              'desafio14.',
              'desafio15.']

Nchallenges = 0  # Numero de desafios
Cchallenges = 11  # contador de desafios
random.shuffle(challenges)

while Cchallenges <= 15:
    print()
    choice = str(input(f'Está pronto(A) para o {Cchallenges}° desafio?')).upper().strip()
    print()
    while choice not in 'SIM':
        choice = str(input('Você só tem a opção de dizer sim, então... ')).upper().strip()
    print(f'O seu desafio é {challenges[Nchallenges]} ')
    Nchallenges += 1
    time.sleep(5)
    Cchallenges += 1

print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print()
print('                                     \033[1;40mESTE AGORA É O NIVEL FULL'
      ' MEGA PESADO PROIBIDÃO DA DEEP WEB!\033[m')
print('                                               \033[1;40mDESEJO BOA SORTE,'
      ' POIS VOCÊS VÃO PRECISAR.\033[m')

print()
print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print('\033[1;38m===\033[m' * 40)
print()

challenges = ['desafio 16.',
              'desafio17.',
              'desafio18.',
              'desafio19.',
              'desafio20.']

Nchallenges = 0  # Numero de desafios
Cchallenges = 16  # contador de desafios
random.shuffle(challenges)

while Cchallenges <= 20:
    print()
    choice = str(input(f'Está pronto(A) para o {Cchallenges}° desafio?')).upper().strip()
    print()
    while choice not in 'SIM':
        choice = str(input('Você só tem a opção de dizer sim, então... ')).upper().strip()
    print(f'O seu desafio é {challenges[Nchallenges]} ')
    Nchallenges += 1
    time.sleep(5)
    Cchallenges += 1

print()
print()
print('FIM DE JOGO')
