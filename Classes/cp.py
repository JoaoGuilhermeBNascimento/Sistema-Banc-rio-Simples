from Classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            # se o saldo for menor que o valor que a pessoa está sacando, não é para sacar retornar error.
            print(f' Saldo insuficiente para o saque, você tem R${self.saldo}')
            return

        self.saldo -= valor
        self.detalhes()
