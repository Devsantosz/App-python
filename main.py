from Cliente import Cliente
from Conta import Conta
from tkinter import *
#Tkinter para tela, com objetivo de criar exibicao

class main:
    pass

c1 = Cliente("João","19 99999-9999")
conta1 = Conta(c1.get_nome(),0000)

c2 = Cliente("Guilherme","19 88888-8888")
conta2 = Conta(c2.get_nome(),1111)

conta1.depositar(100)
conta1.tranferir(conta2, 25)
conta1.extrato()

conta2.extrato()


