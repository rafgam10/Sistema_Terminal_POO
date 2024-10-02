from cadastro import *

class Login:

    #Construtor:
    def __init__(self, codigo:str, senha:str):
        self.codigo=codigo
        self.senha=senha
        self.listaUsuario = []
        self.listaProduto = []

    #Método de Verificação:
    def VerificarLogin(self, codigoInput:str, senhaInput:str):
        if(codigoInput == self.codigo and senhaInput == self.senha):
            print("Acesso liberado.")
        else:
            print("Acesso negado.")
            print("Tente logan novamnte.")

    #Método de Cadastro de Usuário:
    def CadastroUsuario(self, codigoInput, nomeInput, senhaInput):
        status = False
        for i in self.listaUsuario:
            if self.listaUsuario.codigo != codigoInput:
                status = True
            else:
                status = False

        if status:
            var=Usuario(codigoInput, nomeInput, senhaInput)
            self.listaUsuario.append(var)
            print(f"Usuário Criando com Sucesso!")

    #Método de Cadastro de Produto:
    def CadastroProduto(self, codigoInput, nomeInput, categoriaInput, quantidadeInput, precoInput):
        status = False
        for i in self.listaProduto:
            if self.listaProduto.codigo != codigoInput:
                status = True
            else:
                status = False

        if status:
            var=Produto(codigoInput, nomeInput, categoriaInput, quantidadeInput, precoInput)
            self.listaProduto.append(var)
            print(f"Produto Criando com Sucesso!")

    




