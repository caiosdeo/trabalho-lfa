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

class Teste:

    def __init__(self):
        self.inicializar()
        self.testarInclusao()
        self.testarIgualdade()
        self.testeUniaoIntersecao()

    def inicializar(self):
        self.e1 = Estado("e1")
        self.e2 = Estado("e2")
        self.e3 = Estado("e3")
        self.e4 = Estado("e4")
            
        self.s1 = Simbolo('a')
        self.s2 = Simbolo('b')
        self.s3 = Simbolo('c')
        
        self.t1 = TransicaoD()
        self.t1.setOrigem(self.e1)
        self.t1.setSimbolo(self.s1)
        self.t1.setDestino(self.e2)
        
        self.t2 = TransicaoD()
        self.t2.setOrigem(self.e3)
        self.t2.setSimbolo(self.s1)
        self.t2.setDestino(self.e2)
        
        self.t3 = TransicaoD()
        self.t3.setOrigem(self.e2)
        self.t3.setSimbolo(self.s2)
        self.t3.setDestino(self.e3)
        
        self.ce = ConjuntoEstados()
        self.ce2 = ConjuntoEstados()
        
        self.csi = ConjuntoSimbolos()
        self.csi2 = ConjuntoSimbolos()
        
        self.ct = ConjuntoTransicaoD()
        self.ct2 = ConjuntoTransicaoD()
        
        self.cce = ConjuntoConjuntoEstados()
        self.cce2 = ConjuntoConjuntoEstados()

    def testarInclusao(self):
        self.ce.inclui(self.e1)
        self.ce.inclui(self.e2)
        self.ce.inclui(self.e3)			
        
        self.ce2.inclui(self.e1)
        self.ce2.inclui(self.e2)
        self.ce2.inclui(self.e3)
        self.ce2.inclui(self.e4)
        
        self.csi.inclui(self.s1)
        self.csi.inclui(self.s2)
        self.csi2.inclui(self.s3)
        
        self.ct.inclui(self.t1)
        self.ct.inclui(self.t3)
        self.ct2.inclui(self.t2)
        
        self.cce.inclui(self.ce)
        self.cce.inclui(self.ce2)
        self.cce2.inclui(self.ce)
        
        print("Teste inclusao: ")
        print(f"ce: {self.ce} \nce2: {self.ce2} \ncsi: {self.csi} \nct: {self.ct} \ncce: {self.cce}")

    def testeUniaoIntersecao(self):

        ceTeste = ConjuntoEstados()
        csTeste = ConjuntoSimbolos()
        ctTeste = ConjuntoTransicaoD()
        cceTeste = ConjuntoConjuntoEstados()

        ceTeste = self.ce.uniao(self.ce2)		
        print(f"ceUce2: {ceTeste}")
        
        ceTeste = self.ce.intersecao(self.ce2)		
        print(f"ceIce2: {ceTeste}")
        
        csTeste = self.csi.uniao(self.csi2)		
        print(f"csiUcsi2: {csTeste}")
        
        csTeste = self.csi.intersecao(self.csi2)		
        print(f"csiIcsi2: {csTeste}")
        
        ctTeste = self.ct.uniao(self.ct2)		
        print(f"ctUct2: {ctTeste}")
        
        ctTeste = self.ct.intersecao(self.ct2)		
        print(f"ctIct2: {ctTeste}")
        
        cceTeste = self.cce.uniao(self.cce2)		
        print(f"cceUcce2: {cceTeste}")
        
        cceTeste = self.cce.intersecao(self.cce2)		
        print(f"cceIcce2: {cceTeste}")

    def testarIgualdade(self):

        if(self.ce.igual(self.ce2)):
            print("Conjunto de estados iguais")
        else:
            print("Conjunto de estados diferentes")
        
        if(self.csi.igual(self.csi2)):
            print("Conjunto de simbolos iguais")
        else:
            print("Conjunto de simbolos diferentes")
        
        if(self.ct.igual(self.ct2)):
            print("Conjunto de transicaoD iguais")
        else:
            print("Conjunto de transicaoD diferentes")
        
        if(self.cce.igual(self.cce)):
            print("ConjuntoConjuntoEstados iguais")
        else:
            print("ConjuntoConjuntoEstados diferentes")
		

if __name__ == '__main__':
    teste = Teste()