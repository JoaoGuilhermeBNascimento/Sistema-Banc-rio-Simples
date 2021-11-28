from Classes.cc import ContaCorrente
from Classes.cp import ContaPoupanca
from Classes.banco import Banco
from Classes.cliente import Cliente


banco = Banco()

cliente1 = Cliente('João', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('Luiz', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254136, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print()

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')

# cc = ContaCorrente(agencia= 12087, conta= 22190, saldo = 0, limite=200)
# cc.depositar(50)
# cc.sacar(250)
# cc.depositar(1000)
# print()
# print('Conta Poupança.. Information')
# cp = ContaPoupanca(12086, conta= 22000,saldo=100)
# cp.depositar(1000)