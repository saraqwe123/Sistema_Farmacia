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
        nomeRemedio = input("Qual é o nome do remédio?: ")
        ean13 = input("Qual é o ean13 do remédio?: ")
        ncm = int(input("Qual é o ncm do remédio?: "))
        precoVenda = float(input("Qual é o preço do remédio?: "))
        fabricante = input("Qual é o fabricante do remédio?: ")
        substancia = input("Qual é a substância do remédio?: ")
        registroMS = input("Qual é o registro MS do remédio?: ")
        #sql = "insert INTO Remedio (registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia
        return remedio.Remedio(registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia)