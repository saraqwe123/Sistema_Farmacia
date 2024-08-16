import ENTITIES.Remedio as remedio
from DAO.ControleBD import ControleBD

class RemedioDAO:
    def __cursorListaDeRemedio(self, cursor): 
        cursor = ControleBD()
        linha = cursor.fetchone() #Criando linhas
        listaDeLinhas = [] #Lista vazia para armazenar linhas
    
        for i in range(len(linha)):
            listaDeLinhas.append(self.__pegaInfoRemedio(linha)) #Coloca cada linha do bd na lista

        return listaDeLinhas
    
    def __pegaInfoRemedio(self, linha):
        rem = remedio.Remedio() 
        #Cada linha do bd transformado em Objeto
        rem.nomeRemedio = linha["nome"]
        rem.ean13 = linha["ean13"]
        rem.fabricante = linha["fabricante"]
        rem.ncm = linha["ncm"]
        rem.precoVenda = linha["preço de venda"]
        rem.registroMS = linha["registro MS"]
        rem.substancia = linha["substancia"]
        return rem

    def criaRemedio(self):
        medicamento = remedio.Remedio()
        return medicamento

    def retorna(self, ean13):
        cursor = ControleBD().cursor()
        query = ""
        cursor.execute(query, ean13)
        linha = cursor.fetchone()
        
        if linha is not None:
            return self.__pegaInfoRemedio(linha)
        
        else:
            return None
        
    def atualiza(self, ean13):
        cursor = ControleBD().cursor()
        droga = remedio.Remedio()
        
        if hasattr(droga, "ean13"):
            atualizacao = ""
            cursor.execute(atualizacao)
        
        else:
            criar = ""
            cursor.execute(criar)
        
        cursor.close()        
        return True

"""
    #def update(self, produto):
    #  connection = DBController().obterConnection();
    #  cursor = connection.cursor()
    #
    #  if not hasattr(produto, 'id'):
    #    cursor.execute('INSERT INTO Produto (nome, quantidade, validade, precoUltimaCompra, dataFabricacao) VALUES(?, ?, ?, ?, ?, ?)',
    #      nome, quantidade, validade, descricao, precoUltimaCompra, dataFabricacao)
    #  else:
    #    cursor.execute('UPDATE Produto SET nome=?, quantidade=?, validade=?, precoUltimaCompra=?, dataFabricacao=? WHERE id = ?',
    #      nome, quantidade, validade, descricao, precoUltimaCompra, dataFabricacao, id)
    # 
    #  cursor.close()
    #  connection.close()
    #  return True

    def delete(self, produto):
        return None

    def listByNome(self, nome):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM Produto WHERE nome = ?', nome)
      
      result = self.__cursorToListOfProduto(cursor)
     
      cursor.close()
      connection.close()

      return result

    def listByEan13(self, ean13):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM Produto WHERE ean13 = ?', ean13)
      
      result = self.__cursorToListOfProduto(cursor)
     
      cursor.close()
      connection.close()

      return result
"""