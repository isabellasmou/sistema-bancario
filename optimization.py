class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.usuarios = []
        self.contas = []
        self.numero_conta = 1

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        
        for usuario in self.usuarios:
            if usuario['cpf'] == cpf:
                print('CPF já cadastrado. Não é possível cadastrar o usuário.')
                return
        
        
        cpf = cpf.replace('.', '').replace('-', '')

        usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        self.usuarios.append(usuario)
        print('Usuário cadastrado com sucesso.')

    def cadastrar_conta(self, cpf):
        
        usuarios_encontrados = [usuario for usuario in self.usuarios if usuario['cpf'] == cpf]

        if len(usuarios_encontrados) == 0:
            print('Usuário não encontrado. Não é possível cadastrar a conta.')
            return

        usuario = usuarios_encontrados[0]

        conta = {
            'agencia': '0001',
            'numero': self.numero_conta,
            'usuario': usuario
        }
        self.contas.append(conta)
        self.numero_conta += 1
        print(f'Conta cadastrada com sucesso. Número da conta: {conta["numero"]}')

    def deposito(self, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

        return saldo, extrato

    def saque(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        if saldo >= valor and valor <= limite and numero_saques < limite_saques:
            saldo -= valor
            extrato.append(-valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        elif valor > limite:
            print('O valor máximo de saque é R$ 500.00.')
        else:
            print('Limite máximo de saques diários atingido.')

        return saldo, extrato

    def extrato(self, extrato):
        print('Extrato:')
        print('Movimentações realizadas:')
        for movimentacao in extrato:
            if movimentacao > 0:
                print(f'Depósito de R$ {movimentacao:.2f}')
            else:
                print(f'Saque de R$ {-movimentacao:.2f}')
        print(f'Saldo atual: R$ {sum(extrato):.2f}')

    def listar_contas(self):
        print('Contas cadastradas:')
        for conta in self.contas:
            print(f'Número da conta: {conta["numero"]}')
            print(f'Agência: {conta["agencia"]}')
            print(f'Usuário: {conta["usuario"]["nome"]}')
            print('---')

def main():
    banco = Banco()
    while True:
        print('Escolha uma operação:')
        print('u - Cadastrar Usuário')
        print('c - Cadastrar Conta')
        print('d - Depositar')
        print('s - Sacar')
        print('e - Extrato')
        print('l - Listar Contas')
        print('q - Sair')

        operacao = input('Operação: ')

        if operacao == 'u':
            nome = input('Digite o nome do usuário: ')
            data_nascimento = input('Digite a data de nascimento do usuário: ')
            cpf = input('Digite o CPF do usuário: ')
            endereco = input('Digite o endereço do usuário: ')
            banco.cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif operacao == 'c':
            cpf = input('Digite o CPF do usuário para cadastrar a conta: ')
            banco.cadastrar_conta(cpf)
        elif operacao == 'd':
            valor = float(input('Digite o valor do depósito: '))
            banco.saldo, banco.depositos = banco.deposito(banco.saldo, valor, banco.depositos)
        elif operacao == 's':
            valor = float(input('Digite o valor do saque: '))
            banco.saldo, banco.saques = banco.saque(
                saldo=banco.saldo,
                valor=valor,
                extrato=banco.saques,
                limite=500,
                numero_saques=len(banco.saques),
                limite_saques=3
            )
        elif operacao == 'e':
            banco.extrato(banco.depositos + banco.saques)
        elif operacao == 'l':
            banco.listar_contas()
        elif operacao == 'q':
            break
        else:
            print('Operação inválida. Por favor, tente novamente.')


if __name__ == '__main__':
    main()
