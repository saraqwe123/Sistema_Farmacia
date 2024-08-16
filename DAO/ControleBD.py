import psycopg2


class ControleBD:
    def __init__(self):
        self.conexao = psycopg2.connect(host = "localhost", bdNome = "SistemaFarmacia", senha = "natipedro14", usuario = "postgres", porta = "5432")
        return self.conexao
        
    def cursor(self):
        return self.conexao.cursor()

    def commit(self):
        return self.conexao.commit()

    def close(self):
        return self.conexao.close()