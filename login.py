class Login:

    #Construtor:
    def __init__(self, codigo:str, senha:str):
        self.codigo=codigo
        self.senha=senha

    #Método de Verificação:
    def VerificarLogin(self, codigoInput:str, senhaInput:str):
        if(codigoInput == self.codigo and senhaInput == self.senha):
            print("Acesso liberado.")
        else:
            print("Acesso negado.")
            print("Tente logan novamnte.")

    

    




