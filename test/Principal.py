# Importando classes
from src.classes.Simbolo import Simbolo
from src.classes.Estado import Estado
from src.classes.TransicaoD import TransicaoD
from src.classes.TransicaoN import TransicaoN
from src.classes.ConjuntoEstados import ConjuntoEstados
from src.classes.ConjuntoTransicaoD import ConjuntoTransicaoD
from src.classes.ConjuntoTransicaoN import ConjuntoTransicaoN
from src.classes.ConjuntoSimbolo import ConjuntoSimbolos
from src.classes.ConjuntoConjuntoEstados import ConjuntoConjuntoEstados
from src.classes.AFD import AFD
from src.classes.AFN import AFN

class Principal:

    def __init__(self):
        print("AFD Testes:")
        self.testeAFD()
        print("AFN Testes:")
        self.testeAFN()

    def testeAFD(self):
        estadoInicial = Estado()
        estadosFinais = ConjuntoEstados()
        estados = ConjuntoEstados()
        funcaoPrograma = ConjuntoTransicaoD()
        simbolos = ConjuntoSimbolos()
        a = AFD(simbolos, estados, funcaoPrograma, estadoInicial, estadosFinais)
        w = "abaaaa"
        
        a.lerXML("./test/AFD.XML")
        
        # print(a)
        # a.gera(a.getEstadoInicial(), "") # TODO: Checar essa função
        if (a.aceita(w)):
            print(f"Aceitou {w}")
        print(f"Pe(q0, {w}): {a.pe(a.getEstadoInicial(), w)}")       

        a.exportarXML("testeAFDexp")

    def testeAFN(self):
        estadoInicial = Estado()
        estadosFinais = ConjuntoEstados()
        estados = ConjuntoEstados()
        funcaoPrograma = ConjuntoTransicaoN()
        simbolos = ConjuntoSimbolos()
        a = AFN(simbolos, estados, funcaoPrograma, estadoInicial, estadosFinais)

        a.lerXML("./test/AFN.XML")
        # print(a)
        # print(a.toAFD())
        a.exportarXML("testeAFNexp")

if __name__ == '__main__':
    teste = Principal()