from DAO.RemedioDAO import RemedioDAO
from DAO.CategoriaDAO import CategoriaDAO
from DVO.RemedioDVO import CodigoBarraEAN13
from DAO.FornecedorDAO import FornecedorDAO


class RemedioMGR:
    def buscaRemedio(self, nomeRemedio):
        self.dvoRem = CodigoBarraEAN13()
        self.daoRem = RemedioDAO()
        self.daoRem.listaPorNome(nomeRemedio)

    def buscaCategoria(self, categoria):
        if CategoriaDAO().categoriaExiste(categoria):
            return True
        return False
    
    def buscaFornecedor(self, fornecedor):
        if FornecedorDAO().fornecedorExiste(fornecedor):
            return True
        return False
    
    def cadastroRemedio(self, remedio, categoria, fornecedor):
        if self.buscaCategoria(categoria) and self.buscaFornecedor(fornecedor):
            self.dvoRem.validarEAN13()
            self.dvoRem.verificaNCM()
            self.dvoRem.verificaSubstanciaMS()
            self.daoRem.criaRemedio()
            self.daoRem.pegaInfoRemedio()
            return self.daoRem.atualizaOuCria(remedio)
        
mgr = RemedioMGR()
mgr.cadastroRemedio()
