from DAO.ControleBD import ControleBD
from ENTITIES.Fornecedor import Fornecedor

class FornecedorDAO:
    def __cursorListaFornecedor(self, cursor):
        cursor = ControleBD().cursor()
        linha = cursor.fetchone()
        resultado = []
        while linha is not None:
            resultado.append(self)
            
    def pegaInfoFornecedor(self, linha):
        Fornecedores = Fornecedor()
        Fornecedores.dataCadastro = linha["dataCadastro"]
        Fornecedores.nomeSocio = linha["nomeSocio"]
        Fornecedores.endereco = linha["endereco"]
        Fornecedores.email = linha["email"]
        Fornecedores.nomeFornecedor = linha["nomeFornecedor"]
        Fornecedores.bairro = linha["bairro"]
        Fornecedores.cep = linha["cep"]
        Fornecedores.cidade = linha["cidade"]
        Fornecedores.cnpj = linha["cnpj"]
        Fornecedores.complemento = linha["complemento"]
        Fornecedores.numero = linha["numero"]
        Fornecedores.infc = linha["infc"]
        Fornecedores.telefone = linha["telefone"]
        
        
