class Conta:#Cria conta
    #Atriubutos da conta
    def __init__(self, titular, numero, saldo=0):
        #self. representa o proprio objeto
        self._titular = titular
        self.numero = numero
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    #Nao deixa o saldo ser menor que 0
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo!")
        else:
            self._saldo = saldo
    #verifica se tem saldo e saca o valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    #Verifica se o valor é maior que 0 e entao deposita
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
    #Transfere
    def tranferir(self, destino, valor):
        if valor <= 0:
            print("O valor tem que ser maior que zero!")
        elif self.saldo >= valor:
            self.saldo -= valor
            destino.depositar(valor)
            print("'Transferencia realizada com sucesso!")
        else:
            print("Saldo insuficiente!")

    #Mostra o extrato, com os valores do nome, num da conta e o saldo
    def extrato(self):
        print("Cliente:", self._titular)
        print("Número da conta:", self.numero)
        print("Saldo atual:", self.saldo)