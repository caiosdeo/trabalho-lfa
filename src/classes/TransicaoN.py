import Estado
import ConjuntoEstados
import Simbolo

class TransicaoN:

    def __init__(self, origem='', destino='', simbolo=''):
        """Construtor da TransicaoN

        Args:
            origem (Estado): Estado origem da TransicaoN
            destino (ConjuntoEstados): Conjunto de Estados destinos da TransicaoN
            simbolo (Simbolo): Simbolo da TransicaoN 
        """
        self.origem = Estado()
        self.destino = Estado()
        self.simbolo = Simbolo()
        
    def getDestino(self):
        """Obtem o Estado destino da TransicaoN

        Returns:
            destino (Estado): Estado destino da transicao
        """
        return self.destino.clonar()

    def setDestino(self, destino):
        """Ajusta o Estado destino da TransicaoN

        Args:
            destino (ConjuntoEstados): Novo Conjunto de Estados destinos da Transicao    
        """
        self.destino = destino.clonar()

    def getOrigem(self):
        """Obtem o Estado origem da TransicaoN

        Returns:
            origem (Estado): Estado origem da transicao
        """
        if self.origem != None:
            return self.origem.clonar()
        return None

    def setOrigem(self, origem):
        """Ajusta o Estado origem da TransicaoN

        Args:
            origem (Estado): Novo Estado de origem da Transicao    
        """
        self.origem = origem.clonar()
    
    def getSimbolo(self):
        """Obtem o simbolo da TransicaoN

        Returns:
            simbolo (Simbolo): Simbolo da transicao
        """
        return self.simbolo.clonar()

    def setSimbolo(self, simbolo):
        """Ajusta o Simbolo da TransicaoN

        Args:
            simbolo (Simbolo): Novo Simbolo da Transicao    
        """        
        self.simbolo = simbolo.clonar()

    def clonar(self):
        """Cria e retorna uma copia do objeto TransicaoN

        Returns:
            tn (TransicaoN): clone da TransicaoN
        """
        tn = TransicaoN(self.origem, self.destino, self.simbolo)
        return tn

    def igual(self, transicao):
        """Verifica se a TransicaoN passada por parametro é igual a propria TransicaoN
        
        Args:
            transicao (TransicaoN): TransicaoN a ser comparada

        Returns:
            igual (bool): flag para igualdade das transicoes
                (default é False)
        """
        if (self.destino.igual(transicao.getDestino()) and self.origem.igual(transicao.getOrigem()) and self.simbolo.igual(transicao.getSimbolo())):
            return True
        return False

    def __str__(self):
        return "(" + self.origem + ", " + self.destino + ", " + self.simbolo + ")"
