import ENTITIES.Remedio as remedio
import ENTITIES.Categoria as categoria
from DAO.ControleBD import ControleBD

class RemedioDAO:
    def __cursorListaDeRemedio(self, cursor): 
        cursor = ControleBD().cursor()
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
        rem.dcb = linha["descricaoDCB"]
        rem.quantidadeUnitaria = linha["quantidadeUnitaria"]
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
        
    def atualizaOuCria(self, rem):
        cursor = ControleBD().cursor()
        droga = remedio.Remedio()
        
        if hasattr(rem, "ean13"):
            atualizacao = ("UPDATE Remedio SET nomeRemedio=?, ean13=?, ncm=?, precoVenda=?, fabricante=?, registroMS=?, substancia=? WHERE ean13=?", droga.nomeRemedio, droga.ean13, droga.ncm, droga.precoVenda, droga.fabricante, droga.registroMS, droga.substancia)
            cursor.execute(atualizacao)
        
        else:
            criar = "INSERT INTO Remedio (nomeRemedio, ean13, ncm, precoVenda, fabricante, registroMS, substancia) VALUES (?,?,?,?,?,?,?)", droga.nomeRemedio, droga.ean13, droga.ncm, droga.precoVenda, droga.fabricante, droga.registroMS, droga.substancia
            cursor.execute(criar)
        
        cursor.close()        
        return True
    
    
    def delete(self, rem):
        cursor = ControleBD().cursor()
        droga = remedio.Remedio()
        
        if hasattr(rem, "ean13"):
            deletacao = ("DELETE Remedio SET nomeRemedio=?, ean13=?, ncm=?, precoVenda=?, fabricante=?, registroMS=?, substancia=? WHERE ean13=?", droga.ean13)
            cursor.execute(deletacao)
        
        else:
            return "Não foi possível encontrar o remédio solicitado"
         
        cursor.close()        
        return True
    
    
    def listaPorNomeOuCategoria(self, nomeRemedioOuCategoria):
        cursor = ControleBD().cursor()
        droga = remedio.Remedio()
        cat = categoria.Categoria()

        if hasattr(nomeRemedioOuCategoria, "nomeRemedio"):
            buscaNome = ("SELECT * FROM Remedio WHERE nome = ?", droga.nomeRemedio)
            return cursor.execute(buscaNome)
        
        else:
            buscaCategoria = ("SELECT * FROM Remedio WHERE nome = ?", cat.categoria)
            return cursor.execute(buscaCategoria)
