from DAO.RemedioDAO import RemedioDAO
from DVO.RemedioDVO import CodigoBarraEAN13

class RemedioMGR:
    def consultaEstoque(self, nomeRemedioOuEAN13):
        self.dvoRem = CodigoBarraEAN13()
        self.daoRem = RemedioDAO()
        if self.dvoRem.validar(): # Retorna um valor booleano se é ou não um ean13
            return self.daoRem.listaPorNomeOuEAN13(nomeRemedioOuEAN13)
        else:
            return self.daoRem.listaPorNomeOuEAN13(nomeRemedioOuEAN13)

    def cadastroRemedio(self, remedio):
        return self.daoRem.atualizaOuCria(remedio)