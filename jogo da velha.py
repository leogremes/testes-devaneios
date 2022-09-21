from random import choice


# DEF PARA MOSTRAR O DISPLAY DO CAMPO QUANDO NECESSÁRIO
def show_display(inst=False):
    if inst:
        print(''' 
    7 | 8 | 9 
   ---+---+--- 
    4 | 5 | 6     >>>    O TABULEIRO ESPELHA O TECLADO NUMÉRICO!
   ---+---+---
    1 | 2 | 3 
 ''')
    else:
        print(f''' 
    {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} 
   ---+---+--- 
    {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} 
   ---+---+---
    {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} 
        ''')


# LISTAS E VARIÁVEIS
jogadores = dict()
tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
cond_vitoria = ['012', '345', '678', '036', '147', '258', '048', '246']
vitx = vito = empates = jogos = 0

# CABEÇALHO
print('=' * 80)
print('JOGO DA VELHA BOLADÃO'.center(80))
print('=' * 80)

# PEGANDO NOME DOS JOGADORES
print()
print('O primeiro jogador é escolhido aleatóriamente')
print()
jogadores['X'] = input('Nome do jogador "X" => ').strip().upper()
jogadores['O'] = input('Nome do Jogador "O" => ').strip().upper()
print()

# SORTEIO DO PRIMEIRO JOGADOR
vez = choice(('X', 'O'))
print(f'O jogador {jogadores[vez]} - \'{vez}\' começa.')

# COMEÇANDO O JOGO
while True:
    # MOSTRAR O DISPLAY DE INSTRUÇÕES
    show_display(True)

    # ZERANDO GANHADOR E EMPATE ANTES DO JOGO
    ganhador = empate = False

    while True:

        # LAÇO DE REPETIÇÃO PRA VALIDAR A JOGADA
        while True:

            jogada = input(f'Jogada atual: {jogadores[vez]} ({vez}). Escolha onde deseja jogar => ').strip()

            # VERIFICA SE É NÚMERO
            if jogada.isnumeric():
                jogada = int(jogada) - 1

                # VERIFICA SE ESTÁ EM UM INTERVALO VÁLIDO
                if 0 <= jogada <= 8:

                    # VERIFICA SE A CASA ESTÁ LIVRE
                    if tabuleiro[jogada] == ' ':
                        tabuleiro[jogada] = vez
                        break

                    else:
                        print('Esta casa já está ocupada')

                else:
                    print('Intervalo Inválido')

            else:
                print('Não é um número válido')

        # VERIFICANDO SE O JOGO FOI GANHO
        for cond in cond_vitoria:
            if tabuleiro[int(cond[0])] == tabuleiro[int(cond[1])] == tabuleiro[int(cond[2])] != ' ':
                ganhador = True
                break

        show_display()

        # VERIFICANDO SE O JOGO EMPATOU
        if tabuleiro.count(' ') == 0:
            empate = True

        # SAINDO DA REPETIÇÃO SE HOUVER GANHADOR
        if ganhador or empate:
            break

        # INVERTENDO A VEZ PARA O PRÓXIMO LANCE
        vez = 'X' if vez == 'O' else 'O'

    # TÉRMINO DO JOGO
    print('FIM DE JOGO')
    jogos += 1

    # MOSTRANDO GANHADOR E SOMANDO PLACAR
    if ganhador:
        if vez == 'X':
            vitx += 1
        else:
            vito += 1
        print(f'Vitória de >>>>>  {jogadores[vez]}  <<<<<')

    else:
        empates += 1
        print('Empate!')

    # MOSTRANDO PLACAR
    print('~' * 40)
    print(f'''Número de jogos: {jogos}
Vitórias de {jogadores["X"]} (X): {vitx}
Vitórias de {jogadores["O"]} (O): {vito}
Empates: {empates}''')
    print('~' * 40)

    # VERIFICANDO SE DESEJAM JOGAR OUTRA PARTIDA
    resp = input('Desejam jogar outra ([S][1] - SIM // [N][0] - NÃO)? ').strip().upper()
    while True:
        if resp in ('0', '1', 'S', 'N'):
            break
        resp = input('Opção Incorreta! Por favor, selecione uma opção válida. ')

    if resp in ('0', 'N'):
        break

    # INVERTENDO A VEZ PRA COMEÇAR OUTRA PARTIDA
    vez = 'X' if vez == 'O' else 'O'

    tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('~' * 80)
print('FIM DE JOGO. OBRIGADO E VOLTE SEMPRE :)')
