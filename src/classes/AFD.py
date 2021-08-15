# Importando outras classes
from src.classes.Simbolo import Simbolo
from src.classes.Estado import Estado
from src.classes.TransicaoD import TransicaoD

# Biblioteca para trabalhar com XML
import xml.etree.ElementTree as ET

class AFD:
    
    def __init__(self, simbolos, estados, funcaoPrograma, estadoInicial, estadosFinais):
        """Construtor da AFD

        Args:
            simbolos (ConjuntoSimbolos): ConjuntoSimbolo que representa o alfabeto do automato finito deterministico 
            estados (ConjuntoEstados): ConjuntoEstados que representa o conjunto de estados do automato finito deterministico
            funcaoPrograma (ConjuntoTransicaoD): ConjuntoTransicaoD que representa a funcao programa do automato finito deterministico
            estadoInicial (Estado): Estado que representa o estado inicial do automato finito deterministico
            estadosFinais (ConjuntoEstados): ConjuntoEstados que representa o conjunto de estados finais do automato finito deterministico
        """
        self.simbolos = simbolos.clonar()
        self.estados = estados.clonar()
        self.funcaoPrograma = funcaoPrograma.clonar()
        self.estadoInicial = estadoInicial.clonar()
        self.estadosFinais = estadosFinais.clonar()

    def getEstadoInicial(self):
        """Obtem o estado inicial do automato finito deterministico

        Retorno:
            estadoInicial (Estado): Estado que representa o estado inicial do automato finito deterministico
        """
        return self.estadoInicial.clonar()

    def setEstadoInicial(self, estadoInicial):
        """Ajusta o estado inicial do automato finito deterministico para o valor passado como parametro

        Args:
            estadoInicial (Estado): um Estado a ser definido como estado inicial do automato finito deterministico
        """  
        self.estadoInicial = estadoInicial

    def getEstados(self):
        """Obtem o conjunto de estados do automato finito deterministico

        Retorno:
            estados (ConjuntoEstados): representa o conjunto de estados do automato finito deterministico
        """
        return self.estados.clonar()

    def setEstados(self, estados):
        """Ajusta o conjunto de estados do automato finito deterministico para o valor passado como parametro

        Args:
            estados (ConjuntoEstados): a ser definido como conjunto de estados do automato finito deterministico
        """  
        self.estados = estados

    def getEstadosFinais(self):
        """Obtem o conjunto de estados finais do automato finito deterministico

        Retorno:
            estadosFinais (ConjuntoEstados): representa o conjunto de estados finais do automato finito deterministico
        """
        return self.estadosFinais.clonar()

    def setEstadosFinais(self, estadosFinais):
        """Ajusta o conjunto de estados finais do automato finito deterministico para o valor passado como parametro

        Args:
            estadosFinais (ConjuntoEstados): a ser definido como conjunto de estados finais do automato finito deterministico
        """  
        self.estadosFinais = estadosFinais

    def getFuncaoPrograma(self):
        """Obtem a funcao programa do automato finito deterministico

        Retorno:
            funcaoPrograma (ConjuntoTransicaoD): representa a funcao programa do automato finito deterministico
        """
        return self.funcaoPrograma.clonar()

    def setEstadosFinais(self, funcaoPrograma):
        """Ajusta a funcao programa do automato finito deterministico para o valor passado como parametro

        Args:
            funcaoPrograma (ConjuntoTransicaoD): a ser definido como a funcao programa do automato finito deterministico
        """  
        self.funcaoPrograma = funcaoPrograma 

    def getSimbolos(self):
        """Obtem o alfabeto do automato finito deterministico

        Retorno:
            simbolos (ConjuntoSimbolo): representa o alfabeto do automato finito deterministico
        """
        return self.simbolos.clonar()

    def setSimbolos(self, simbolos):
        """Ajusta o alfabeto do automato finito deterministico para o valor passado como parametro

        Args:
            simbolos (ConjuntoSimbolo): a ser definido como o alfabeto do automato finito deterministico
        """  
        self.simbolos = simbolos   

    def clonar(self):
        """Clona o automato finito deterministico

        Retorno:
            afd (AFD): representa o automato finito deterministico
        """
        afd = AFD(self.simbolos, self.estados, self.funcaoPrograma, self.estadoInicial, self.estadosFinais)
        return afd

    def __str__(self):
        return f"({self.simbolos}, {self.estados}, {self.funcaoPrograma}, {self.estadoInicial}, {self.estadosFinais})"

    def limpa(self):
        """Limpa as estruturas de dados do AFD""" 
        
        self.simbolos.limpar()
        self.estados.limpar()
        self.funcaoPrograma.limpar()
        self.estadoInicial.limpar()
        self.estadosFinais.limpar()

    def gera(self, estado, palavra):
        """Algoritmo para geracao de L(M), sendo M um AFD. É feita uma impressão de L(M).
        
        Args:
            estado (Estado): estado do automato finito deterministico
            palavra (String): palavra para impressão de L(M)
        """

        if (self.estadosFinais.pertence(estado)):
            print(palavra + "\n")

        ct = self.getFuncaoPrograma()
        t = None

        if (not ct.vazio()):
            if len(ct) > 0:
                tAux = ct[1]
                ct.removerElemento(tAux)
                t = tAux

        # Para cada transição do AFD
        while (t != None):
            aux = palavra  
            if (t.getOrigem().igual(estado)):
                #  Acrescenta o simbolo a palavra
                aux = aux + t.getSimbolo()
                #  Se a palavra for maior que 10
                if (len(aux > 10)):
                    print("...\n")
                    break
                else:
                    # Continua compondo a palavra a partir do estado atingido
                    self.gera(t.getDestino(), aux)
            
            if (not ct.vazio()):
                if len(ct) > 0:
                    tAux = ct[1]
                    ct.removerElemento(tAux)
                    t = tAux
            else:
                t = None

    def p(self, estado, simbolo):
        """Função Programa
        
        Args:
            estado (Estado): estado que vai dar inicio ao processamento
            simbolo (Simbolo): simbolo a ser processado

        Retorno:
            estadoAlcancado (Estado): estado alcancavel depois de processar o simbolo a partir do estado dado 
        """

        fp = self.getFuncaoPrograma()
        for it in fp.getElementos().values():
            if (it.getOrigem().igual(estado) and it.getSimbolo().igual(simbolo)):
                return it.getDestino()

        return Estado()

    def pe(self, estado, palavra):
        """Função Programa Estendida
        
        Args:
            estado (Estado): estado que vai dar inicio ao processamento
            palavra (String): palavra a ser processado

        Retorno:
            estadoAlcancado (Estado): estado alcancavel depois de processar a palavra a partir do estado dado
        """

        estadoAtual = estado
        i = 0

        while i < len(palavra):

            simbolo = Simbolo(palavra[i])
            estadoAtual = self.p(estadoAtual, simbolo)
            if estadoAtual == None:
                return None
            i += 1

        return estadoAtual

    def aceita(self, palavra):
        """Retorna se uma palavra e aceita ou nao pelo AFD
        
        Args:
            palavra (String): palavra a ser verificada

        Retorno:
            pertence (bool): flag para pertencimento da palavra no AFD
                (default é False)
        """
        
        return self.estadosFinais.pertence(self.pe(self.estadoInicial, palavra))

    def lerXML(self, caminhoArquivo):
        """Le as informacoes de um AFD em um arquivo XML passado como parametro e atribui as informacoes no objeto
        
        Args:
            caminhoArquivo (String): caminho do arquivo XML a ser lido
        """

        root = ET.parse(caminhoArquivo).getroot()

        # Pegando o estado inicial
        self.estadoInicial = Estado(str(root.find("estadoInicial").get('valor')))

        # Resgatando o restante das informações
        for parametro in root:

            if(parametro.tag == "simbolos"):
                for elemento in parametro:
                    simbolo = Simbolo(str(elemento.get('valor')))
                    self.simbolos.inclui(simbolo)    

            if(parametro.tag == "estados"):
                for elemento in parametro:
                    estado = Estado(str(elemento.get('valor')))
                    self.estados.inclui(estado) 

            if(parametro.tag == "funcaoPrograma"):
                for elemento in parametro:
                    origem = Estado(str(elemento.get('origem')))
                    destino = Estado(str(elemento.get('destino')))
                    simbolo = Simbolo(str(elemento.get('simbolo')))
                    transicao = TransicaoD()
                    transicao.setOrigem(origem)
                    transicao.setDestino(destino)
                    transicao.setSimbolo(simbolo)
                    self.funcaoPrograma.inclui(transicao)   

            if(parametro.tag == "estadosFinais"):
                for elemento in parametro:
                    estado = Estado(str(elemento.get('valor')))
                    self.estadosFinais.inclui(estado)

    def exportarXML(self, nomeArquivo):
        """Cria arquivo XML do AFD com nome passado por parametro
        
        Args:
            nomeArquivo (String): nome do arquivo XML a ser criado
        """

        # Raiz do XML
        afd = ET.Element('AFD')

        # Simbolos
        simbolos = ET.SubElement(afd, 'simbolos')
        for simbolo in self.simbolos.getElementos():
            aux = ET.SubElement(simbolos, 'elemento')
            aux.set('valor', str(simbolo))

        # Estados
        estados = ET.SubElement(afd, 'estados')
        for estado in self.estados.getElementos():
            aux = ET.SubElement(estados, 'elemento')
            aux.set('valor', str(estado))

        # Estados Finais
        estadosFinais = ET.SubElement(afd, 'estadosFinais')
        for estadoFinal in self.estadosFinais.getElementos():
            aux = ET.SubElement(estadosFinais, 'elemento')
            aux.set('valor', str(estadoFinal))

        # Funcao Programa
        funcaoPrograma = ET.SubElement(afd, 'funcaoPrograma')
        for transicao in self.funcaoPrograma.getElementos().items():
            aux = ET.SubElement(funcaoPrograma, 'elemento')
            aux.set('destino', str(transicao[1].getDestino()))
            aux.set('origem', str(transicao[1].getOrigem()))
            aux.set('simbolo', str(transicao[1].getSimbolo()))

        # Estado Inicial
        estadoInicial = ET.SubElement(afd, 'estadoInicial')
        estadoInicial.set('valor', str(self.estadoInicial))

        # cria o arquivo XML
        afdTree = ET.tostring(afd).decode()
        arquivo = open(nomeArquivo + ".xml", "w")
        arquivo.write(afdTree)