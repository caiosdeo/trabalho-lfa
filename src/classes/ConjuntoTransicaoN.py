from collections import OrderedDict

class ConjuntoTransicaoN:

    """Inicializa a classe ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
    """
    def __init__(self):
        self.elementos = OrderedDict()

    """Verifica se um ConjuntoTransicaoN está ou não vazio

    Args:
        self (ConjuntoTransicaoN): A própria classe

    Returns:
        bool: True se estiver vazio, False caso contrário
    """
    def vazio(self):
        return False if self.elementos else True

    """Inclui um elemento no final do ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
        elemento (TransicaoN): TransicaoN a ser inserida no ConjuntoTransicaoN
    """
    def inclui(self,elemento):
        self.elementos[elemento.toString()] = elemento.clonar()

    """Verfica se uma TransicaoN pertence a um dado ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
        elemento (TransicaoN): TransicaoN a ser verificada

    Returns:
        bool: True se pertence, False caso contrário
    """
    def pertence(self,elemento):
        if elemento is not None:
            return True if elemento.toString() in self.elementos.keys() else False
        return False

    """Realiza a união entre dois ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
        ctn (ConjuntoTransicaoN): um ConjuntoTransicaoN a ser unido a outro

    Returns:
        ConjuntoTransicaoN: ConjuntoTransicaoN resultante da união
    """
    def uniao(self,ctn):
        novoConjunto = self.clonar()
        for key in ctn.getElementos.keys():
            e = ctn.getElementos[key]
            if not novoConjunto.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Realiza a interseção entre dois ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
        ctn (ConjuntoTransicaoN): um ConjuntoTransicaoN a sofrer interseção com outro ConjuntoTransicaoN

    Returns:
        ConjuntoTransicaoN: ConjuntoTransicaoN resultante da interseção
    """
    def interseção(self,ctn):
        novoConjunto = ConjuntoTransicaoN()
        for key in ctn.getElementos.keys():
            e = ctn.getElementos[key]
            if self.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Cria e retorna uma cópia do objeto ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe

    Returns:
        ConjuntoTransicaoN: um clone do próprio objeto
    """
    def clonar(self):
        novoConjunto = ConjuntoTransicaoN()
        for key in self.elementos.keys():
            novoConjunto.inclui(self.elementos[key].clonar())
        return novoConjunto

    """Verifica se dois conjuntos são iguais

    Args:
        self (ConjuntoTransicaoN): A própria classe
        ctn (ConjuntoTransicaoN): um ConjuntoTransicaoN a ser verificado

    Returns:
        bool: True se forem iguais, False caso contrário
    """
    def igual(self,ctn):
        for key in ctn.getElementos.keys():
            e = ctn.getElementos[key]
            if not self.pertence(e):
                return False
        for key in self.elementos.keys():
            e = self.elementos[key]
            if not ctn.pertence(e):
                return False
        return True 

    """Esse método tem como função pegar todos os nomes dos elementos do conjunto
       e colocar em uma string

    Args:
        self (ConjuntoTransicaoN): A própria classe

    Returns:
        str: string contendo os nomes dos elementos do conjunto
    """
    def toString(self):
        return '{' + f"{','.join(self.elementos.keys())}" + '}'

    """Esse método tem como função retornar os elementos de um ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe

    Returns:
        OrderedDict: elementos do ConjuntoTransicaoN
    """
    def getElementos(self):
        return self.elementos

    """Esse método remove um elemento do ConjuntoTransicaoN

    Args:
        self (ConjuntoTransicaoN): A própria classe
    """
    def removerElemento(self,e):
        if e is not None:
            del self.elementos[e.toString()]
	