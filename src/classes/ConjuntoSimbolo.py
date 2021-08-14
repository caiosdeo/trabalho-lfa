from collections import OrderedDict

class ConjuntoSimbolos:

    """Inicializa a classe ConjuntoSimbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
    """
    def __init__(self):
        self.elementos = OrderedDict()

    """Verifica se um conjunto de símbolos está ou não vazio

    Args:
        self (ConjuntoSimbolos): A própria classe

    Returns:
        bool: True se estiver vazio, False caso contrário
    """
    def vazio(self):
        return False if self.elementos else True

    """Limpa o conjunto de símbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
    """
    def limpar(self):
        self.elementos.clear()

    """Inclui um elemento no final do conjunto de símbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
        elemento (Símbolo): Símbolo a ser inserido no conjunto de símbolos
    """
    def inclui(self,elemento):
        self.elementos[elemento.getSimbolo()] = elemento.clonar()

    """Verfica se um Simbolo pertence a um dado conjunto de símbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
        elemento (Simbolo): Simbolo a ser verificado

    Returns:
        bool: True se pertence, False caso contrário
    """
    def pertence(self,elemento):
        if elemento is not None:
            return True if elemento.getSimbolo() in self.elementos.keys() else False
        return False

    """Cria e retorna uma cópia do objeto ConjuntoSimbolos

    Args:
        self (ConjuntoSimbolos): A própria classe

    Returns:
        ConjuntoSimbolos: um clone do próprio objeto
    """
    def clonar(self):
        novoConjunto = ConjuntoSimbolos()
        for key in self.elementos.keys():
            novoConjunto.inclui(self.elementos[key].clonar())
        return novoConjunto

    """Realiza a união entre dois conjuntos de Simbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
        cs (ConjuntoSimbolos): um ConjuntoSimbolos a ser unido a outro

    Returns:
        ConjuntoSimbolos: ConjuntoSimbolos resultante da união
    """
    def uniao(self,cs):
        novoConjunto = self.clonar()
        csElementos = cs.getElementos()
        for key in csElementos.keys():
            e = csElementos[key]
            if not novoConjunto.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Realiza a interseção entre dois conjuntos de Simbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
        cs (ConjuntoSimbolos): um ConjuntoSimbolos a sofrer interseção com outro ConjuntoSimbolos

    Returns:
        ConjuntoSimbolos: ConjuntoSimbolos resultante da interseção
    """
    def interseção(self,cs):
        novoConjunto = ConjuntoSimbolos()
        csElementos = cs.getElementos()
        for key in csElementos.keys():
            e = csElementos[key]
            if self.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Verifica se dois conjuntos são iguais

    Args:
        self (ConjuntoSimbolos): A própria classe
        cs (ConjuntoSimbolos): um ConjuntoSimbolos a ser verificado

    Returns:
        bool: True se forem iguais, False caso contrário
    """
    def igual(self,cs):
        csElementos = cs.getElementos()
        for key in csElementos.keys():
            e = csElementos[key]
            if not self.pertence(e):
                return False
        for key in self.elementos.keys():
            e = self.elementos[key]
            if not cs.pertence(e):
                return False
        return True 

    """Esse método tem como função pegar todos os nomes dos elementos do conjunto
       e colocar em uma string

    Args:
        self (ConjuntoSimbolos): A própria classe

    Returns:
        str: string contendo os nomes dos elementos do conjunto
    """
    def toString(self):
        return '{' + f"{','.join(self.elementos.keys())}" + '}'

    """Esse método tem como função retornar os elementos de um ConjuntoSimbolos

    Args:
        self (ConjuntoSimbolos): A própria classe

    Returns:
        OrderedDict: elementos do ConjuntoSimbolos
    """
    def getElementos(self):
        return self.elementos

    """Esse método remove um elemento do ConjuntoSimbolos

    Args:
        self (ConjuntoSimbolos): A própria classe
    """
    def removerElemento(self,e):
        if e is not None:
            del self.elementos[e.getSimbolo()]
	