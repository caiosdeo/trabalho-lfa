from src.classes.Simbolo import Simbolo
from src.classes.Estado import Estado

class TransicaoD:

    def __init__(self):
        """Construtor da TransicaoD
        """
        self.origem = Estado()
        self.destino = Estado()
        self.simbolo = Simbolo()
        
    def getDestino(self):
        """Obtem o Estado destino da TransicaoD

        Retorno:
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

        Retorno:
            origem (Estado): Estado origem da transicao
        """
        if self.origem != None:
            return self.origem.clonar()
        return None

    def setOrigem(self, origem):
        """Ajusta o Estado origem da TransicaoD

        Args:
            origem (Estado): Novo Estado de origem da Transicao    
        """
        self.origem = origem.clonar()
    
    def getSimbolo(self):
        """Obtem o simbolo da TransicaoD

        Retorno:
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

        Retorno:
            td (TransicaoD): clone da TransicaoD
        """
        td = TransicaoD()
        td.setOrigem(self.origem)
        td.setDestino(self.destino)
        td.setSimbolo(self.simbolo)
        return td

    def igual(self, transicao):
        """Verifica se a TransicaoD passada por parametro é igual a propria TransicaoD
        
        Args:
            transicao (TransicaoD): TransicaoD a ser comparada

        Retorno:
            igual (bool): flag para igualdade das transicoes
                (default é False)
        """
        if (self.destino.igual(transicao.getDestino()) and self.origem.igual(transicao.getOrigem()) and self.simbolo.igual(transicao.getSimbolo())):
            return True
        return False

    def __str__(self):
        return f"( {self.origem}, {self.destino}, {self.simbolo})"