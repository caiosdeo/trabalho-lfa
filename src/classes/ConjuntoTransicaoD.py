from collections import OrderedDict

class ConjuntoTransicaoD:

    """Inicializa a classe ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
    """
    def __init__(self):
        self.elementos = OrderedDict()

    """Verifica se um ConjuntoTransicaoD está ou não vazio

    Args:
        self (ConjuntoTransicaoD): A própria classe

    Returns:
        bool: True se estiver vazio, False caso contrário
    """
    def vazio(self):
        return False if self.elementos else True

    """Inclui um elemento no final do ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
        elemento (TransicaoN): TransicaoN a ser inserida no ConjuntoTransicaoD
    """
    def inclui(self,elemento):
        self.elementos[elemento.__str__()] = elemento.clonar()

    """Verfica se uma TransicaoN pertence a um dado ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
        elemento (TransicaoN): TransicaoN a ser verificada

    Returns:
        bool: True se pertence, False caso contrário
    """
    def pertence(self,elemento):
        if elemento is not None:
            return True if elemento.__str__() in self.elementos.keys() else False
        return False

    """Realiza a união entre dois ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
        ctn (ConjuntoTransicaoD): um ConjuntoTransicaoD a ser unido a outro

    Returns:
        ConjuntoTransicaoD: ConjuntoTransicaoD resultante da união
    """
    def uniao(self,ctn):
        novoConjunto = self.clonar()
        ctnElementos = ctn.getElementos()
        for key in ctnElementos.keys():
            e = ctnElementos[key]
            if not novoConjunto.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Realiza a interseção entre dois ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
        ctn (ConjuntoTransicaoD): um ConjuntoTransicaoD a sofrer interseção com outro ConjuntoTransicaoD

    Returns:
        ConjuntoTransicaoD: ConjuntoTransicaoD resultante da interseção
    """
    def intersecao(self,ctn):
        novoConjunto = ConjuntoTransicaoD()
        ctnElementos = ctn.getElementos()
        for key in ctnElementos.keys():
            e = ctnElementos[key]
            if self.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Cria e retorna uma cópia do objeto ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe

    Returns:
        ConjuntoTransicaoD: um clone do próprio objeto
    """
    def clonar(self):
        novoConjunto = ConjuntoTransicaoD()
        for key in self.elementos.keys():
            novoConjunto.inclui(self.elementos[key].clonar())
        return novoConjunto

    """Verifica se dois conjuntos são iguais

    Args:
        self (ConjuntoTransicaoD): A própria classe
        ctn (ConjuntoTransicaoD): um ConjuntoTransicaoD a ser verificado

    Returns:
        bool: True se forem iguais, False caso contrário
    """
    def igual(self,ctn):
        ctnElementos = ctn.getElementos()
        for key in ctnElementos.keys():
            e = ctnElementos[key]
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
        self (ConjuntoTransicaoD): A própria classe

    Returns:
        str: string contendo os nomes dos elementos do conjunto
    """
    def __str__(self):
        return '{' + f"{','.join(self.elementos.keys())}" + '}'

    """Esse método tem como função retornar os elementos de um ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe

    Returns:
        OrderedDict: elementos do ConjuntoTransicaoD
    """
    def getElementos(self):
        return self.elementos

    """Esse método remove um elemento do ConjuntoTransicaoD

    Args:
        self (ConjuntoTransicaoD): A própria classe
    """
    def removerElemento(self,e):
        if e is not None:
            del self.elementos[e.__str__()]
	