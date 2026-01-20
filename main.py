class main:
    pass
print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João","19 99283-5421")
conta = Conta(c1.nome,6565,0)

print(conta.titular," Número: ", conta.numero, " Saldo: ", conta.saldo)
