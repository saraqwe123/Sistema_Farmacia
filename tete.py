class Person: 
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.endereco = ""
     
    
class Pf(Person): 
    def __init__(self):
        super().__init__()
        self.cpf = ""
     

pessoa = Person()

pessoa.nome = "Sara"    
pessoa.email = "Saraguaiume@gmail.com"
pessoa.endereco = "Rua Mato Grosso, 390"

pessoaFisica = Pf()
pessoaFisica.nome = pessoa.nome
pessoaFisica.cpf = "11122233344"

print(pessoaFisica.nome)


def div(a, b):
    try:
        return a/b
    
    except Exception as e:
        return f"erro: {e}"
    

print(div(1, 0))