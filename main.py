from termcolor import cprint, colored
from operacoes.soma import Soma
from operacoes.subtracao import Subtracao
from operacoes.divisao import Divisao
from operacoes.multiplicacao import Multiplicacao

def menu():
    cprint('-='*75, 'yellow')
    return int(input(colored('Qual operação você deseja fazer?\n1) Soma\n2) Subtração\n3) Divisão\n4) Multiplicação\n5) Parar\n>>>', 'blue')))
    cprint('-=' * 75, 'yellow')


def pedir_numero1(n1):
    return int(input(colored(f'Informe o 1° número: ', 'yellow')))


def pedir_numero2(n2):
    return int(input(colored(f'Informe o 2° número: ', 'yellow')))


n1 = 0
n2 = 0


def rodar_calculadora(n1, n2):
    laço = True
    while laço:
        cls()
        escolha = menu()
        cprint('-=' * 75, 'yellow')
        if escolha == 5:
            cprint('Espero que tenha gostado, até mais!', 'green', attrs=['underline'])
            cprint('-=' * 75, 'yellow')
            break
        if escolha > 5:
            cprint('Cara, eu te dei 5 opções...', 'red')
            rodar_calculadora(n1, n2)
        n1 = pedir_numero1(n1)
        n2 = pedir_numero2(n2)
        cprint('-=' * 75, 'yellow')
        if escolha == 1:
            soma = Soma(n1, n2)
            cprint(f'{n1} + {n2} = {soma.result}', 'green')
        if escolha == 2:
            subtracao = Subtracao(n1, n2)
            cprint(f'{n1} - {n2} = {subtracao.result}', 'green')
        if escolha == 3:
            divisao = Divisao(n1, n2)
            cprint(f'{n1} / {n2} = {divisao.result}', 'green')
        if escolha == 4:
            multiplicacao = Multiplicacao(n1, n2)
            cprint(f'{n1} * {n2} = {multiplicacao.result}', 'green')


rodar_calculadora(n1, n2)






