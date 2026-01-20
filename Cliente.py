class Cliente:
    def __init__(self, n,telefone):

         self._nome = n
         self._telefone = telefone


#Metodo get
    def get_nome(self):
        return self._nome

#Metodo set
    def set_nome(self, nome):
        self._nome = nome