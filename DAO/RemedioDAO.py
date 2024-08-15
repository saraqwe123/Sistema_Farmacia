import ENTITIES.Remedio as remedio
from DAO.ControleBD import ControleBD
class RemedioDAO:
    def __cursorListaDeRemedio(self, cursor):
        conexao = ControleBD()
        linha = conexao.fetchone()
        listaDeLinhas = []
        
        for i in range(len(linha)):
            listaDeLinhas.append(self.gravarBD(linha))

        return listaDeLinhas




    def gravarBD(self, linha):
        rem = remedio.Remedio()
        rem.nomeRemedio = linha["nome"]
        rem.ean13 = linha["ean13"]
        rem.fabricante = linha["fabricante"]
        rem.ncm = linha["ncm"]
        rem.precoVenda = linha["preço de venda"]
        rem.registroMS = linha["registro MS"]
        rem.substancia = linha["substancia"]