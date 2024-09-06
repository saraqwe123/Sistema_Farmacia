"""from daos.ProdutoDao import ProdutoDao
from dvos.ProdutoDvo import ProdutoDvo

class EstoqueMgr:
    def consultarEstoque(self, nomeOuEan13):
      if ProdutoDvo().isEan13(nomeOuEan13): # Retorna um valor booleano se é ou não um ean13
        return ProdutoDao().listByEan13(nomeOuEan13)
      else:
        return ProdutoDao().listByNome(nomeOuEan13)

    def cadastrarProduto(self, produto):
      ProdutoDao().update(produto) # Adiciona no bd
"""

from DAO.RemedioDAO import RemedioDAO
from DVO.RemedioDVO import RemedioDVO

class RemedioMGR:
    pass