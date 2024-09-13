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

    def categoriaExiste(self, categoria):
        query = "SELECT * FROM categoria WHERE categoria = ?"
        cursor = ControleBD().cursor()
        cursor.execute(query, (categoria))
        resultado = cursor.fetchone()
        return resultado is not None
