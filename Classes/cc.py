from Classes.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=200) -> None:
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print('Saldo insuficiente para o saque')
            return
        
        self._saldo -= valor
        self.detalhes()
        