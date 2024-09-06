from DAO.ControleBD import ControleBD
import ENTITIES.Categoria as categoria

class CategoriaDAO:
    def __cursorListaCategoria(self, cursor):
        cursor = ControleBD().cursor()
        linha = cursor.fetchone()
        resultado = []
        while linha is not None:
            resultado.append(self)
            
    def pegaInfoCategoria(self, linha):
        categorias = categoria.Categoria()
        categorias.categoria = linha["categoria"]
        