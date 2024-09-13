from DAO.RemedioDAO import RemedioDAO
from DAO.CategoriaDAO import CategoriaDAO
from DVO.RemedioDVO import CodigoBarraEAN13


class RemedioMGR:
    def buscaRemedio(self, nomeRemedio):
        self.dvoRem = CodigoBarraEAN13()
        self.daoRem = RemedioDAO()
        self.daoRem.listaPorNome(nomeRemedio)

    def cadastroRemedio(self, remedio):
        if CategoriaDAO()
        self.dvoRem.validarEAN13()
        self.dvoRem.verificaNCM()
        self.dvoRem.verificaSubstanciaMS()
        self.daoRem.criaRemedio()
        self.daoRem.pegaInfoRemedio()
        return self.daoRem.atualizaOuCria(remedio)
    
    def buscaFornecedor(self, fornecedor):
        pass
    
mgr = RemedioMGR()
mgr.cadastroRemedio()
