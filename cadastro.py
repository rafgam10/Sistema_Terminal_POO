class Usuario:

    def __init__(self, codigo: str, nome: str, senha: str):
        self.codigo = codigo
        self.nome = nome
        self.senha = senha


class Produto(Usuario):
    
    def __init__(self, codigo: str, nome: str, categoria: str, quantidade: int, preco:float):
        super().__init__(codigo, nome)


