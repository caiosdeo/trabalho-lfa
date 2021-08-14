# Importando outras classes
from src.classes.Simbolo import Simbolo
from src.classes.Estado import Estado
from src.classes.TransicaoD import TransicaoD
from src.classes.TransicaoN import TransicaoN
from src.classes.ConjuntoEstados import ConjuntoEstados
from src.classes.ConjuntoTransicaoD import ConjuntoTransicaoD
from src.classes.ConjuntoConjuntoEstados import ConjuntoConjuntoEstados
from src.classes.AFD import AFD

# Biblioteca para trabalhar com XML
import xml.etree.ElementTree as ET

class AFN:
    
    def __init__(self, simbolos, estados, funcaoPrograma, estadoInicial, estadosFinais):
        """Construtor do AFN

        Args:
            simbolos (ConjuntoSimbolos): ConjuntoSimbolo que representa o alfabeto do automato finito nao-deterministico 
            estados (ConjuntoEstados): ConjuntoEstados que representa o conjunto de estados do automato finito nao-deterministico
            funcaoPrograma (ConjuntoTransicaoN): ConjuntoTransicaoD que representa a funcao programa do automato finito nao-deterministico
            estadoInicial (Estado): Estado que representa o estado inicial do automato finito nao-deterministico
            estadosFinais (ConjuntoEstados): ConjuntoEstados que representa o conjunto de estados finais do automato finito nao-deterministico
        """
        self.simbolos = simbolos.clonar()
        self.estados = estados.clonar()
        self.funcaoPrograma = funcaoPrograma.clonar()
        self.estadoInicial = estadoInicial.clonar()
        self.estadosFinais = estadosFinais.clonar()

    def getEstadoInicial(self):
        """Obtem o estado inicial do automato finito nao-deterministico

        Retorno:
            estadoInicial (Estado): Estado que representa o estado inicial do automato finito nao-deterministico
        """
        return self.estadoInicial.clonar()

    def setEstadoInicial(self, estadoInicial):
        """Ajusta o estado inicial do automato finito nao-deterministico para o valor passado como parametro

        Args:
            estadoInicial (Estado): um Estado a ser definido como estado inicial do automato finito nao-deterministico
        """  
        self.estadoInicial = estadoInicial

    def getEstados(self):
        """Obtem o conjunto de estados do automato finito nao-deterministico

        Retorno:
            estados (ConjuntoEstados): representa o conjunto de estados do automato finito nao-deterministico
        """
        return self.estados.clonar()

    def setEstados(self, estados):
        """Ajusta o conjunto de estados do automato finito nao-deterministico para o valor passado como parametro

        Args:
            estados (ConjuntoEstados): a ser definido como conjunto de estados do automato finito nao-deterministico
        """  
        self.estados = estados

    def getEstadosFinais(self):
        """Obtem o conjunto de estados finais do automato finito nao-deterministico

        Retorno:
            estadosFinais (ConjuntoEstados): representa o conjunto de estados finais do automato finito nao-deterministico
        """
        return self.estadosFinais.clonar()

    def setEstadosFinais(self, estadosFinais):
        """Ajusta o conjunto de estados finais do automato finito nao-deterministico para o valor passado como parametro

        Args:
            estadosFinais (ConjuntoEstados): a ser definido como conjunto de estados finais do automato finito nao-deterministico
        """  
        self.estadosFinais = estadosFinais

    def getFuncaoPrograma(self):
        """Obtem a funcao programa do automato finito nao-deterministico

        Retorno:
            funcaoPrograma (ConjuntoTransicaoN): representa a funcao programa do automato finito nao-deterministico
        """
        return self.funcaoPrograma.clonar()

    def setEstadosFinais(self, funcaoPrograma):
        """Ajusta a funcao programa do automato finito nao-deterministico para o valor passado como parametro

        Args:
            funcaoPrograma (ConjuntoTransicaoN): a ser definido como a funcao programa do automato finito nao-deterministico
        """  
        self.funcaoPrograma = funcaoPrograma 

    def getSimbolos(self):
        """Obtem o alfabeto do automato finito nao-deterministico

        Retorno:
            simbolos (ConjuntoSimbolo): representa o alfabeto do automato finito nao-deterministico
        """
        return self.simbolos.clonar()

    def setSimbolos(self, simbolos):
        """Ajusta o alfabeto do automato finito nao-deterministico para o valor passado como parametro

        Args:
            simbolos (ConjuntoSimbolo): a ser definido como o alfabeto do automato finito nao-deterministico
        """  
        self.simbolos = simbolos   

    def clonar(self):
        """Clona o automato finito nao-deterministico

        Retorno:
            afn (AFD): representa o automato finito nao-deterministico
        """
        afn = self.afn(self.simbolos, self.estados, self.funcaoPrograma, self.estadoInicial, self.estadosFinais)
        return afn

    def __str__(self):
        return "(" + self.simbolos + ", " + self.estados + ", " + self.funcaoPrograma + ", " + self.estadoInicial + ", " + self.estadosFinais + ")"

    def limpa(self):
        """Limpa as estruturas de dados do AFD""" 
        
        self.simbolos.limpar()
        self.estados.limpar()
        self.funcaoPrograma.limpar()
        self.estadoInicial.limpar()
        self.estadosFinais.limpar()

    def p(self, estado, simbolo):
        """Função Programa
        
        Args:
            estado (Estado): estado que vai dar inicio ao processamento
            simbolo (Simbolo): simbolo a ser processado

        Retorno:
            estadoAlcancado (Estado): estado alcancavel depois de processar o simbolo a partir do estado dado 
        """

        fp = self.getFuncaoPrograma()

        for it in fp.getElementos():
            if (it.getOrigem().igual(estado) and it.getSimbolo().igual(simbolo)):
                return it.getDestino()

        return None

    def pe(self, estados, palavra):
        """Função Programa Estendida
        
        Args:
            estado (Estado): estado que vai dar inicio ao processamento
            palavra (String): palavra a ser processado

        Retorno:
            estadoAlcancado (Estado): estado alcancavel depois de processar a palavra a partir do estado dado
        """

        if palavra == "":
            return estados
        else:

            conjuntoNovo = ConjuntoEstados()
            simbolo = Simbolo(palavra[0])

            for it in estados:
                conjuntoNovo = conjuntoNovo.uniao(self.p(it, simbolo))

            return self.pe(conjuntoNovo, palavra[1:''])

    def aceita(self, palavra):
        """Retorna se uma palavra e aceita ou nao pelo AFD
        
        Args:
            palavra (String): palavra a ser verificada

        Retorno:
            pertence (bool): flag para pertencimento da palavra no AFD
                (default é False)
        """

        cestadoInicial = ConjuntoEstados()
        cestadoInicial.inclui(self.getEstadoInicial())
        cestadoFinal = self.getEstadosFinais()

        for it in self.pe(cestadoInicial, palavra):
            if(cestadoFinal.pertence(it)):
                return True

        return False


    # TODO: método toAFD
    def toAFD(self):
        """Converte um AFN em um AFD

        Retorno:
            afd (AFD): AFD equivalente ao AFN
        """

        # Parametros para criar o AFD 
        novoConjuntoSimbolos = self.getSimbolos().clonar()
        novoConjuntoEstados = ConjuntoEstados()
        novoConjuntoTransicaoD = ConjuntoTransicaoD()
        novoEstadoInicial = Estado("<" + self.getEstadoInicial() + ">")
        novoConjuntoEstadosFinais = ConjuntoEstados()
        novoEstado = Estado()
        novaTransicaoD = TransicaoD()

        # Conjunto estados finais atual
        atualConjuntoEstadosFinais = self.getEstadosFinais()

        # Parametros para o controle de fluxo do algoritmo
        cceAtual = ConjuntoConjuntoEstados()
        conjuntoEstadosAtual = ConjuntoEstados()
        estadoAtual = self.getEstadoInicial().clonar()


        # Parametro temporario necessario para criacao do novo Estado
        ceTemp = ConjuntoEstados()

		# Inclusao do estado inicial
        conjuntoEstadosAtual.inclui(estadoAtual)
        cceAtual.inclui(conjuntoEstadosAtual)

        # Inclusão no conjunto de estados finais
        if (atualConjuntoEstadosFinais.pertence(estadoAtual)):
                novoConjuntoEstadosFinais.inclui(novoEstadoInicial)

		novoConjuntoEstados.inclui(novoEstadoInicial)

        # Iteracao sobre os conjuntos de estados que serao analizados
        for it in cceAtual:

            conjuntoEstadosAtual = it

            # Remove o elemento do Conjunto de analisaveis pois este sera analizado
            cceAtual.removerElemento(conjuntoEstadosAtual)
            # Renova o parametro temporario
            ceTemp = ConjuntoEstados()
            # Parametro para verificar se o estado vai pertencer ao conjunto de estados finais
            estadoFinal = False

            # Iteracao sobre o conjunto de simbolos do Alfabeto
            for itSi in novoConjuntoSimbolos:

                # Iteracao sobre os Estados que formam o estado atual
                ceTemp = ConjuntoEstados()

                for itCe in conjuntoEstadosAtual:
                    # Novo estado sera a uniao de todos o retorno da funcao programa para um determinado simbolo
                    ceTemp = ceTemp.uniao(self.p(itCe, itSi))

                # Verifica se a uniao esta vazia
                if not ceTemp.vazio():
                    # Nome do novo estado
                    novoNome = ceTemp
                    # Retira as {} presentes no inicio e final do nome
                    novoNome = novoNome[1:-1]
                    # insere < > 
                    novoEstado = Estado("<" + novoNome + ">")

                    # Verifica se o estado vai pertencer ao Conjunto de estados finais
                    for itEFinal in ceTemp:
                        if atualConjuntoEstadosFinais.pertence(itEFinal):
                            estadoFinal = True

                    # Se no novo Conjunto de Estados nao houver nenhum estado igual ao novo
					# inclui o novo estado e cria nova transicao
                    if not novoConjuntoEstados.pertence(novoConjuntoEstados.retornaIgual(novoEstado)):
                        novoConjuntoEstados.inclui(novoEstado)

                        # Se for estado final inclui no conjunto de estados finais
                        if estadoFinal:
                            novoConjuntoEstadosFinais.inclui(novoEstado)
                            estadoFinal = False
						
                        # Cria nova transicaoD
                        novaTD = TransicaoD()
                        nomeOrigem = conjuntoEstadosAtual
                        nomeOrigem = "<" + nomeOrigem[1:-1] + ">"

						# Busca origem ja existente no novo Conjunto de Estados
                        novaOrigem = novoConjuntoEstados.retornaIgual(Estado(nomeOrigem))
                        novaTD.setOrigem(novaOrigem)
                        novaTD.setSimbolo(itSi)
                        novaTD.setDestino(novoEstado)

                        novoConjuntoTransicaoD.inclui(novaTD.clonar())

                        cceAtual.inclui(ceTemp)

                    # Caso ja exista estado igual no novo conjunto de estados cria somente nova transicao
                    else:
                        novaTD = TransicaoD()
                        nomeOrigem = conjuntoEstadosAtual
                        nomeOrigem = "<" + nomeOrigem[1:-1] + ">"

                        novaOrigem = novoConjuntoEstados.retornaIgual(Estado(nomeOrigem))
                        novaTD.setOrigem(novaOrigem)
                        novaTD.setSimbolo(itSi)
                        novaTD.setDestino(novoEstado)

                        novoConjuntoTransicaoD.inclui(novaTD.clonar())

        novoAFD = AFD(
            novoConjuntoSimbolos,
            novoConjuntoEstados,
            novoConjuntoTransicaoD,
            novoEstadoInicial,
            novoConjuntoEstadosFinais
        )

        return novoAFD

    def lerXML(self, caminhoArquivo):
        """Le as informacoes de um AFN em um arquivo XML passado como parametro e atribui as informacoes no objeto
        
        Args:
            caminhoArquivo (String): caminho do arquivo XML a ser lido
        """

        root = ET.parse(caminhoArquivo).getroot()

        # Pegando o estado inicial
        self.estadoInicial = str(root.find("estadoInicial").get('valor'))

        # Resgatando o restante das informações
        for parametro in root:

            if(parametro.tag == "simbolos"):
                for elemento in parametro:
                    self.simbolos.inclui(str(elemento.get('valor')))    

            if(parametro.tag == "estados"):
                for elemento in parametro:
                    self.estados.inclui(str(elemento.get('valor'))) 

            if(parametro.tag == "funcaoPrograma"):
                for elemento in parametro:
                    origem = str(elemento.get('origem'))
                    destino = str(elemento.get('destino'))
                    simbolo = str(elemento.get('simbolo'))

                    transicao = TransicaoN()
                    transicao.setOrigem(origem)
                    transicao.setSimbolo(simbolo)

                    for it in self.funcaoPrograma:
                        if it.getOrigem().igual(transicao.getOrigem()) and it.getSimbolo().igual(transicao.getSimbolo()):
                            transicao.setDestino(it.getDestino())
                            self.funcaoPrograma.removerElemento(it)
                            break
                    
                    conjuntoEstados = transicao.getDestino()
                    conjuntoEstados.inclui(Estado(destino))
                    transicao.setDestino(conjuntoEstados)
                    
                    self.funcaoPrograma.inclui(transicao)   

            if(parametro.tag == "estadosFinais"):
                for elemento in parametro:
                    self.estadosFinais.inclui(str(elemento.get('valor')))

    def exportarXML(self, nomeArquivo):
        """Cria arquivo XML do AFN com nome passado por parametro
        
        Args:
            nomeArquivo (String): nome do arquivo XML a ser criado
        """

        # Raiz do XML
        afn = ET.Element('AFN')

        # Simbolos
        simbolos = ET.SubElement(afn, 'simbolos')
        for simbolo in self.simbolos:
            aux = ET.SubElement(simbolos, 'elemento')
            aux.set('valor', simbolo)

        # Estados
        estados = ET.SubElement(afn, 'estados')
        for estado in self.estados:
            aux = ET.SubElement(estados, 'elemento')
            aux.set('valor', estado)

        # Estados Finais
        estadosFinais = ET.SubElement(afn, 'estadosFinais')
        for estadoFinal in self.estadosFinais:
            aux = ET.SubElement(estadosFinais, 'elemento')
            aux.set('valor', estadoFinal)

        # Funcao Programa
        funcaoPrograma = ET.SubElement(afn, 'funcaoPrograma')
        for transicao in self.funcaoPrograma:
            estadosDestino = transicao.getDestino()
            for estado in estadosDestino:
                aux = ET.SubElement(funcaoPrograma, 'elemento')
                aux.set('destino', estado)
                aux.set('origem', transicao.getOrigem())
                aux.set('simbolo', transicao.getSimbolo())

        # Estado Inicial
        estadoInicial = ET.SubElement(afn, 'estadoInicial')
        estadoInicial.set('valor', self.estadoInicial)

        # cria o arquivo XML
        afnTree = ET.tostring(afn)
        arquivo = open(nomeArquivo + ".xml", "w")
        arquivo.write(afnTree)

    # TODO: função lerXML || pesquisar "python xml parser e python render xml as image"
    # TODO: função toXML