from DAO.RemedioDAO import RemedioDAO
from DVO.RemedioDVO import CodigoBarraEAN13

class RemedioMGR:
    def buscaRemedio(self, nomeRemedio):
        self.dvoRem = CodigoBarraEAN13()
        self.daoRem = RemedioDAO()
        self.daoRem.listaPorNome(nomeRemedio)

    def cadastroRemedio(self, remedio):
        self.dvoRem.validarEAN13()
        self.dvoRem.verificaNCM()
        self.dvoRem.verificaSubstanciaMS()
        self.daoRem.criaRemedio()
        self.daoRem.pegaInfoRemedio()
        return self.daoRem.atualizaOuCria(remedio)
    
mgr = RemedioMGR()
mgr.cadastroRemedio()