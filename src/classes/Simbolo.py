class Simbolo:
    VAZIA = Simbolo("E")

    def __init__(self, simbolo=""):
        """Construtor do Simbolo 

        Args:
            simbolo (str): String a ser definida como simbolo do alfabeto 
        """
        self.simbolo = simbolo

    def getSimbolo(self):
        """Obtem o simbolo do alfabeto

        Retorno:
            simbolo (str): String que representa o simbolo do alfabeto
        """
        return self.simbolo

    def setSimbolo(self, simbolo):
        """Ajusta o simbolo do alfabeto para o valor passado como parametro

        Args:
            simbolo (str): String a ser definida como simbolo do alfabeto    
        """
        self.simbolo = simbolo

    def clonar(self):
        """Cria e retorna uma copia do objeto Simbolo

        Retorno:
            s (Simbolo): clone do Simbolo
        """
        s = Simbolo()
        s.setSimbolo(self.getSimbolo())
        return s

    def igual(self, simbolo):
        """Verifica se o Simbolo passado por parametro é igual ao proprio Simbolo
        
        Args:
            simbolo (Simbolo): Simbolo a ser comparado

        Retorno:
            igual (bool): flag para igualdade dos Simbolos
                (default é False)
        """
        if (self.simbolo == simbolo.getSimbolo()):
            return True
        return False
    
    def __str__(self):
        return self.simbolo