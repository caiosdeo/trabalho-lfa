from collections import OrderedDict

class ConjuntoEstados:

    """Inicializa a classe ConjuntoEstados

    Args:
        self (ConjuntoEstados): A própria classe
    """
    def __init__(self):
        self.elementos = OrderedDict()

    """Verifica se um conjunto de estados está ou não vazio

    Args:
        self (ConjuntoEstados): A própria classe

    Returns:
        bool: True se estiver vazio, False caso contrário
    """
    def vazio(self):
        return False if self.elementos else True

    """Limpa o conjunto de estados

    Args:
        self (ConjuntoEstados): A própria classe
    """
    def limpar(self):
        self.elementos.clear()

    """Inclui um elemento no final do conjunto de estados

    Args:
        self (ConjuntoEstados): A própria classe
        elemento (Estado): Estado a ser inserido no conjunto de estados
    """
    def inclui(self,elemento):
        self.elementos[elemento.__str__()] = elemento.clonar()

    """Verfica se um Estado pertence a um dado conjunto de estados

    Args:
        self (ConjuntoEstados): A própria classe
        elemento (Estado): Estado a ser verificado

    Returns:
        bool: True se pertence, False caso contrário
    """
    def pertence(self,elemento):
        if elemento is not None:
            return True if elemento.__str__() in self.elementos.keys() else False
        return False

    """Verfica se um Estado pertence a um dado conjunto de estados
       Se já pertence, retorna o estado que já está contido no conjunto

    Args:
        self (ConjuntoEstados): A própria classe
        elemento (Estado): Estado a ser verificado

    Returns:
        Estado: Retorna um Estado caso o elemento pertença ao conjunto, None caso contrário
    """
    def retornaIgual(self,elemento):
        if elemento is not None:
            if self.pertence(elemento):
                return self.elementos[elemento.__str__()]
            return None
        return None

    """Cria e retorna uma cópia do objeto ConjuntoEstados

    Args:
        self (ConjuntoEstados): A própria classe

    Returns:
        ConjuntoEstados: um clone do próprio objeto
    """
    def clonar(self):
        novoConjunto = ConjuntoEstados()
        for key in self.elementos.keys():
            novoConjunto.inclui(self.elementos[key].clonar())
        return novoConjunto

    """Realiza a união entre dois conjuntos de estados

    Args:
        self (ConjuntoEstados): A própria classe
        ce (ConjuntoEstados): um ConjuntoEstados a ser unido a outro

    Returns:
        ConjuntoEstados: ConjuntoEstados resultante da união
    """
    def uniao(self,ce):
        novoConjunto = self.clonar()
        ceElementos = ce.getElementos()
        for key in ceElementos.keys():
            e = ceElementos[key]
            if not novoConjunto.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Realiza a interseção entre dois conjuntos de estados

    Args:
        self (ConjuntoEstados): A própria classe
        ce (ConjuntoEstados): um ConjuntoEstados a sofrer interseção com outro ConjuntoEstados

    Returns:
        ConjuntoEstados: ConjuntoEstados resultante da interseção
    """
    def intersecao(self,ce):
        novoConjunto = ConjuntoEstados()
        ceElementos = ce.getElementos()
        for key in ceElementos.keys():
            e = ceElementos[key]
            if self.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Verifica se dois conjuntos são iguais

    Args:
        self (ConjuntoEstados): A própria classe
        ce (ConjuntoEstados): um ConjuntoEstados a ser verificado

    Returns:
        bool: True se forem iguais, False caso contrário
    """
    def igual(self,ce):
        ceElementos = ce.getElementos()
        for key in ceElementos.keys():
            e = ceElementos[key]
            if not self.pertence(e):
                return False
        for key in self.elementos.keys():
            e = self.elementos[key]
            if not ce.pertence(e):
                return False
        return True 

    """Esse método tem como função pegar todos os nomes dos elementos do conjunto
       e colocar em uma string

    Args:
        self (ConjuntoEstados): A própria classe

    Returns:
        str: string contendo os nomes dos elementos do conjunto
    """
    def __str__(self):
        return '{' + f"{','.join(self.elementos.keys())}" + '}'

    """Esse método tem como função retornar os elementos de um ConjuntoEstados

    Args:
        self (ConjuntoEstados): A própria classe

    Returns:
        OrderedDict: elementos do ConjuntoEstados
    """
    def getElementos(self):
        return self.elementos

    """Esse método retorna o tamanho do ConjuntoEstados

    Args:
        self (ConjuntoEstados): A própria classe

    Returns:
        int: tamanho do ConjuntoEstados
    """
    def size(self):
        if self.elementos is not None:
            return len(self.elementos)

    """Esse método remove um elemento do ConjuntoEstados

    Args:
        self (ConjuntoEstados): A própria classe
    """
    def removerElemento(self,e):
        if e is not None:
            del self.elementos[e.__str__()]
	