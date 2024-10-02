from login import Login  # Importando a classe Login

# Função principal
def main():
    # Inicializar a instância da classe Login
    sistema = Login(codigo="admin", senha="1234")

    # Exigir login antes de acessar o sistema
    logado = False
    while not logado:
        print("\n===== Tela de Login =====")
        codigoInput = input("Digite o código: ")
        senhaInput = input("Digite a senha: ")
        sistema.VerificarLogin(codigoInput, senhaInput)
        
        # Verifica se o login foi bem-sucedido
        if sistema.usuario_logado:
            logado = True
        else:
            print("Falha no login. Tente novamente.")
    
    # Após login bem-sucedido, exibe o menu principal
    while True:
        print("\n===== Menu Principal =====")
        print("1 - Cadastrar usuário")
        print("2 - Cadastrar produto")
        print("3 - Exibir estoque")
        print("4 - Verificar limite de estoque")
        print("5 - Alterar produto")
        print("6 - Deletar produto")
        print("7 - Sair")
        
        # Recebe a escolha do usuário
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Cadastrar usuário
            codigoInput = input("Digite o código do usuário: ")
            nomeInput = input("Digite o nome do usuário: ")
            senhaInput = input("Digite a senha do usuário: ")
            sistema.CadastroUsuario(codigoInput, nomeInput, senhaInput)

        elif escolha == "2":
            # Cadastrar produto
            codigoInput = input("Digite o código do produto: ")
            nomeInput = input("Digite o nome do produto: ")
            categoriaInput = input("Digite a categoria do produto: ")
            quantidadeInput = int(input("Digite a quantidade: "))
            precoInput = float(input("Digite o preço: "))
            sistema.CadastroProduto(codigoInput, nomeInput, categoriaInput, quantidadeInput, precoInput)

        elif escolha == "3":
            # Exibir porcentagem de estoque
            sistema.ExibirPorcentagemEstoque()

        elif escolha == "4":
            # Verificar limite de estoque
            sistema.VerificarLimiteEstoque()

        elif escolha == "5":
            # Alterar produto
            sistema.AlteracaodoProduto()

        elif escolha == "6":
            # Deletar produto
            sistema.DeletarProduto()

        elif escolha == "7":
            # Sair do programa
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
