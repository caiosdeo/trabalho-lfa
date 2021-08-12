import Estado
import Simbolo

class TransicaoD:

    def __init__(self, origem='', destino='', simbolo=''):
        """Construtor da TransicaoD

        Args:
            origem (Estado): Estado origem da TransicaoD
            destino (Estado): Estado destino da TransicaoD
            simbolo (Simbolo): Simbolo da TransicaoD 
        """
        self.origem = Estado()
        self.destino = Estado()
        self.simbolo = Simbolo()
        
    def getDestino(self):
        """Obtem o Estado destino da TransicaoD

        Returns:
            destino (Estado): Estado destino da transicao
        """
        return self.destino.clonar()

    def setDestino(self, destino):
        """Ajusta o Estado destino da TransicaoD

        Args:
            destino (Estado): Novo Estado de destino da Transicao    
        """
        self.destino = destino.clonar()

    def getOrigem(self):
        """Obtem o Estado origem da TransicaoD

        Returns:
            origem (Estado): Estado origem da transicao
        """
        return self.origem.clonar()

    def setOrigem(self, origem):
        """Ajusta o Estado origem da TransicaoD

        Args:
            origem (Estado): Novo Estado de origem da Transicao    
        """
        self.origem = origem.clonar()
    
    def getSimbolo(self):
        """Obtem o simbolo da TransicaoD

        Returns:
            simbolo (Simbolo): Simbolo da transicao
        """
        return self.simbolo.clonar()

    def setSimbolo(self, simbolo):
        """Ajusta o Simbolo da TransicaoD

        Args:
            simbolo (Simbolo): Novo Simbolo da Transicao    
        """        
        self.simbolo = simbolo.clonar()

    def clonar(self):
        """Cria e retorna uma copia do objeto TransicaoD

        Returns:
            td (TransicaoD): clone da TransicaoD
        """
        td = TransicaoD(self.origem, self.destino, self.simbolo)
        return td

    def igual(self, transicao):
        """Verifica se a TransicaoD passada por parametro é igual a propria TransicaoD
        
        Args:
            transicao (TransicaoD): TransicaoD a ser comparada

        Returns:
            igual (bool): flag para igualdade das transicoes
                (default é False)
        """
        if (self.destino.igual(transicao.getDestino()) and self.origem.igual(transicao.getOrigem()) and self.simbolo.igual(transicao.getSimbolo())):
            return True
        return False

    def __str__(self):
        return "(" + self.origem + ", " + self.destino + ", " + self.simbolo + ")"