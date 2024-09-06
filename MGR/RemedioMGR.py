from DAO.RemedioDAO import RemedioDAO
from DVO.RemedioDVO import CodigoBarraEAN13

class RemedioMGR:
    def buscaRemedio(self, nomeRemedioOuEAN13):
        self.dvoRem = CodigoBarraEAN13()
        self.daoRem = RemedioDAO()
        if self.dvoRem.validarEAN13(): # Retorna um valor booleano se é ou não um ean13
            return f"EAN13: {self.daoRem.listaPorNomeOuEAN13(nomeRemedioOuEAN13)}"
        else:
            return f"nome: {self.daoRem.listaPorNomeOuEAN13(nomeRemedioOuEAN13)}"

    def cadastroRemedio(self, remedio):
        self.dvoRem.validarEAN13()
        self.dvoRem.verificaNCM()
        self.dvoRem.verificaSubstanciaMS()
        self.daoRem.criaRemedio()
        self.daoRem.pegaInfoRemedio()
        return self.daoRem.atualizaOuCria(remedio)
    
mgr = RemedioMGR()
mgr.cadastroRemedio()