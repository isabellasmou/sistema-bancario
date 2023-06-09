# DESAFIO DIO - FORMAÇÃO PYTHON DEVELOPER 

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def saque(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        elif valor > 500:
            print('O valor máximo de saque é R$ 500.00.')
        else:
            print('Limite máximo de saques diários atingido.')

    def extrato(self):
        print('Extrato:')
        print('Depósitos realizados:')
        for deposito in self.depositos:
            print(f'R$ {deposito:.2f}')
        print('Saques realizados:')
        for saque in self.saques:
            print(f'R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')


def main():
    banco = Banco()
    while True:
        print('Escolha uma operação:')
        print('d - Depositar')
        print('s - Sacar')
        print('e - Extrato')
        print('q - Sair')

        operacao = input('Operação: ')

        if operacao == 'd':
            valor = float(input('Digite o valor do depósito: '))
            banco.deposito(valor)
        elif operacao == 's':
            valor = float(input('Digite o valor do saque: '))
            banco.saque(valor)
        elif operacao == 'e':
            banco.extrato()
        elif operacao == 'q':
            break
        else:
            print('Operação inválida. Por favor, tente novamente.')


if __name__ == '__main__':
    main()
