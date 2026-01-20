class main:
    pass
print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João","19 99283-5421")
conta = Conta(c1.get_nome(),1222)

conta.depositar(100)
conta.saque(50)
conta.extrato()


