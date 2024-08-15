import psycopg2


class ControleBD:
    def __init__(self):
        self.conexao = psycopg2.connect(host = "localhost", bdNome = "SistemaFarmacia", senha = "natipedro14", usuario = "postgres", porta = "5432")
        
    def cursor(self):
        self.cur = self.conexao.cursor()

    def commit(self):
        self.cmt = self.conexao.commit()

    def close(self):
        self.cls = self.conexao.close()

    def fetchone(self):
        self.cursor()
        self.linha = self.cur.fetchone()