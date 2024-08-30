"""from daos.DBController import DBController

class ProdutoDao:
    def __cursorToListOfProduto(self, cursor):
      row = cursor.fetchone()
      result = []
      while row is not None:
        result.push(self.__rowToProduto(row))
        row = cursor.fetchone()
      return result

    def __rowToProduto(self, row):
        prod = Produto()
        prod.id(row['id'])
        prod.nome(row['nome'])
        prod.estoque(row['quantidade'])
        prod.validade(row['validade'])
        prod.descricao(row['descricao'])
        prod.precoUltimaCompra(row['precoUltimaCompra'])
        prod.dataFabricacao(row['dataFabricacao'])
        return prod
    """
from DAO.ControleBD import ControleBD
import ENTITIES.Categoria as categoria

class CategoriaDao:
    def __cursorListaCategoria(self, cursor):
        cursor = ControleBD().cursor()
        linha = cursor.fetchone()
        resultado = []
        while linha is not None:
            resultado.append(self)
            
    def PegaInfoCategoria(self, linha):
        categorias = categoria.Categoria()
        