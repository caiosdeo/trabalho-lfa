from collections import OrderedDict
from src.classes.ConjuntoEstados import ConjuntoEstados

class ConjuntoConjuntoEstados:

    """Inicializa a classe ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
    """
    def __init__(self):
        self.elementos = OrderedDict()

    """Verifica se um ConjuntoConjuntoEstados está ou não vazio

    Args:
        self (ConjuntoConjuntoEstados): A própria classe

    Returns:
        bool: True se estiver vazio, False caso contrário
    """
    def vazio(self):
        return False if self.elementos else True

    """Limpa o ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
    """
    def limpar(self):
        self.elementos.clear()

        """Inclui um elemento no final do ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
        elemento (ConjuntoEstado): ConjuntoEstado a ser inserido no ConjuntoConjuntoEstados
    """
    def inclui(self,elemento):
        self.elementos[elemento] = elemento.clonar()

    """Verfica se um ConjuntoEstado pertence a um dado ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
        elemento (ConjuntoEstado): ConjuntoEstado a ser verificado

    Returns:
        bool: True se pertence, False caso contrário
    """
    def pertence(self,elemento):
        if elemento is not None:
            return True if elemento in self.elementos.keys() else False
        return False

    """Realiza a união entre dois ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
        cce (ConjuntoConjuntoEstados): um ConjuntoConjuntoEstados a ser unido a outro

    Returns:
        ConjuntoConjuntoEstados: ConjuntoConjuntoEstados resultante da união
    """
    def uniao(self,cce):
        novoConjunto = self.clonar()
        cceElementos = cce.getElementos()
        for key in cceElementos.keys():
            e = cceElementos[key]
            if not novoConjunto.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Realiza a interseção entre dois ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
        cce (ConjuntoConjuntoEstados): um ConjuntoConjuntoEstados a sofrer interseção com outro ConjuntoConjuntoEstados

    Returns:
        ConjuntoConjuntoEstados: ConjuntoConjuntoEstados resultante da interseção
    """
    def intersecao(self,cce):
        novoConjunto = ConjuntoConjuntoEstados()
        cceElementos = cce.getElementos()
        for key in cceElementos.keys():
            e = cceElementos[key]
            if self.pertence(e):
                novoConjunto.inclui(e.clonar())
        return novoConjunto

    """Cria e retorna uma cópia do objeto ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe

    Returns:
        ConjuntoConjuntoEstados: um clone do próprio objeto
    """
    def clonar(self):
        novoConjunto = ConjuntoConjuntoEstados()
        for key in self.elementos.keys():
            novoConjunto.inclui(self.elementos[key].clonar())
        return novoConjunto

    """Verifica se dois conjuntos são iguais

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
        cce (ConjuntoConjuntoEstados): um ConjuntoConjuntoEstados a ser verificado

    Returns:
        bool: True se forem iguais, False caso contrário
    """
    def igual(self,cce):
        cceElementos = cce.getElementos()
        for key in cceElementos.keys():
            e = cceElementos[key]
            if not self.pertence(e):
                return False
        for key in self.elementos.keys():
            e = self.elementos[key]
            if not cce.pertence(e):
                return False
        return True 

    """Realiza a união entre os elementos do ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe

    Returns:
        ConjuntoEstados: ConjuntoEstados resultante da união
    """
    def uniaoInterna(self):
        novoConjunto = ConjuntoEstados()
        for key in self.elementos.keys():
            e = self.elementos[key]
            novoConjunto.uniao(e)
        return novoConjunto

    """Esse método tem como função pegar todos os nomes dos elementos do conjunto
       e colocar em uma string

    Args:
        self (ConjuntoConjuntoEstados): A própria classe

    Returns:
        str: string contendo os nomes dos elementos do conjunto
    """
    def __str__(self):
        return '{' + f"{','.join(self.elementos.keys())}" + '}'

    """Esse método tem como função retornar os elementos de um ConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe

    Returns:
        OrderedDict: elementos do ConjuntoConjuntoEstados
    """
    def getElementos(self):
        return self.elementos

    """Esse método remove um elemento do ConjuntoConjuntoEstados

    Args:
        self (ConjuntoConjuntoEstados): A própria classe
    """
    def removerElemento(self,e):
        if e is not None:
            del self.elementos[e]
	