class Estado:

    def __init__(self, nome=""):
        """Construtor do Estado 

        Args:
            nome (str): String a ser definida como nome do Estado 
        """
        self.nome = nome

    def getNome(self):
        """Obtem o nome do Estado

        Returns:
            nome (str): String que representa o nome do Estado
        """
        return self.nome

    def setNome(self, nome):
        """Ajusta o nome do Estado para o valor passado como parametro

        Args:
            nome (str): String a ser definida como nome do Estado 
        """
        self.nome = nome

    def clonar(self):
        """Cria e retorna uma copia do objeto Estado

        Returns:
            e (Estado): clone do Estado
        """
        e = Estado()
        e.setNome(self.getNome())
        return e

    def igual(self, estado):
        """Verifica se o Estado passado por parametro é igual ao proprio Estado
        
        Args:
            estado (Estado): Estado a ser comparado 

        Returns:
            igual (bool): flag para igualdade dos Estados
                (default é False)
        """
        if (self.nome == estado.getNome()):
            return True
        return False
    
    def __str__(self):
        return self.nome