from cadastro import *

class Login:

    #Construtor:
    def __init__(self, codigo:str, senha:str):
        self.codigo=codigo
        self.senha=senha
        self.listaUsuario = []
        self.listaProduto = []
        self.usuario_logado = None

        # Declarar constantes para estoque mínimo e máximo por categoria
        self.ESTOQUE_MINIMO = {
            'Eletrônicos': 10,
            'Roupas': 20,
            'Alimentos': 30
        }
        self.ESTOQUE_MAXIMO = {
            'Eletrônicos': 100,
            'Roupas': 200,
            'Alimentos': 300
        }

    #Método de Verificação:
    def VerificarLogin(self, codigoInput: str, senhaInput: str):
        if codigoInput == self.codigo and senhaInput == self.senha:
            self.usuario_logado = True  # Define como True quando o login é bem-sucedido
            print(f"Acesso liberado. Bem-vindo, {codigoInput}!")
        else:
            self.usuario_logado = False  # Define como False se as credenciais estiverem erradas
            print("Acesso negado. Código ou senha incorretos.")

    #Método de Cadastro de Usuário:
    def CadastroUsuario(self, codigoInput, nomeInput, senhaInput):
        status = False
        for i in self.listaUsuario:
            if i.codigo != codigoInput:
                status = True
            else:
                status = False

        if status:
            var=Usuario(codigoInput, nomeInput, senhaInput)
            self.listaUsuario.append(var)
            print(f"Usuário Criando com Sucesso!")

    #Métodos dos Produtos:
    def CadastroProduto(self, codigoInput, nomeInput, categoriaInput, quantidadeInput, precoInput):
        status = False
        for i in self.listaProduto:
            if i.codigo != codigoInput:
                status = True
            else:
                status = False

        if status:
            var=Produto(codigoInput, nomeInput, categoriaInput, quantidadeInput, precoInput)
            self.listaProduto.append(var)
            print(f"Produto Criando com Sucesso!")

    def DeletarProduto(self):
        
        #Exibir todos os Produtos:
        for i in self.listaProduto:
            print(f"Código:{i.codigo} - Nome:{i.nome} - Categoria:{i.categoria}\n")
        
        #Processo de Remoção do Produto:
        codigoInputRemove=str(input("Insira o código do Produto para Remoção:"))
        for i in self.listaProduto:
            
            #Verificação do Produto de Remoção:
            if i.codigo == codigoInputRemove:
                
                print(f"\nProduto que você quer remover:")
                print(f"Código:{i.codigo} - Nome:{i.nome} - Categoria:{i.categoria}\n")
                
                yesNo = str(input("Sim ou Não(S - N):"))
                
                if yesNo == "S":
                    self.listaProduto.remove(i)
                
                else:
                    print(f"Cancelar o Processo de Remoção.")
                break

        print(f"Produto foi Deletado com Sucesso!")


    def AlteracaodoProduto(self):
        # Exibir todos os Produtos:
        for i in self.listaProduto:
            print(f"Código:{i.codigo} - Nome:{i.nome} - Categoria:{i.categoria} - Quantidade:{i.quantidade} - Preço:{i.preco}\n")

        # Selecionar o produto a ser alterado:
        codigoInputAlterar = str(input("Insira o código do Produto que deseja alterar:"))
        for i in self.listaProduto:
            if i.codigo == codigoInputAlterar:
                print(f"Produto selecionado: Código:{i.codigo} - Nome:{i.nome} - Categoria:{i.categoria}\n")

                # Exibir opções de alteração
                print("O que você deseja alterar?")
                print("1 - Código")
                print("2 - Nome")
                print("3 - Categoria")
                print("4 - Quantidade")
                print("5 - Preço")
                escolha = int(input("Escolha uma opção (1-5): "))

                if escolha == 1:
                    novo_codigo = str(input("Digite o novo código: "))
                    i.codigo = novo_codigo
                elif escolha == 2:
                    novo_nome = str(input("Digite o novo nome: "))
                    i.nome = novo_nome
                elif escolha == 3:
                    nova_categoria = str(input("Digite a nova categoria: "))
                    i.categoria = nova_categoria
                elif escolha == 4:
                    nova_quantidade = int(input("Digite a nova quantidade: "))
                    i.quantidade = nova_quantidade
                elif escolha == 5:
                    novo_preco = float(input("Digite o novo preço: "))
                    i.preco = novo_preco
                else:
                    print("Opção inválida!")

                print(f"Produto atualizado: Código:{i.codigo} - Nome:{i.nome} - Categoria:{i.categoria} - Quantidade:{i.quantidade} - Preço:{i.preco}\n")
                break
        else:
            print("Produto não encontrado.") 

    
    # Calcular o total de produtos e o valor total em estoque
    def CalcularEstoqueTotal(self):
        total_quantidade = 0
        total_valor = 0.0

        # Calcular quantidade e valor total dos produtos
        for produto in self.listaProduto:
            total_quantidade += produto.quantidade
            total_valor += produto.quantidade * produto.preco

        return total_quantidade, total_valor

    # Exibir a porcentagem de estoque por categoria
    def ExibirPorcentagemEstoque(self):
        if not self.usuario_logado:
            print("Nenhum usuário está logado.")
            return

        total_quantidade, _ = self.CalcularEstoqueTotal()

        if total_quantidade == 0:
            print("Nenhum produto em estoque.")
            return

        estoque_por_categoria = {}

        # Calcular quantidade de produtos por categoria
        for produto in self.listaProduto:
            if produto.categoria not in estoque_por_categoria:
                estoque_por_categoria[produto.categoria] = 0
            estoque_por_categoria[produto.categoria] += produto.quantidade

        print(f"Estoque por categoria para o usuário {self.usuario_logado}:")
        
        # Exibir a porcentagem de estoque por categoria
        for categoria, quantidade in estoque_por_categoria.items():
            porcentagem = (quantidade / total_quantidade) * 100
            print(f"Categoria: {categoria} - {porcentagem:.2f}% do estoque total")

    # Verificação de limites de estoque
    def VerificarLimiteEstoque(self):
        for produto in self.listaProduto:
            categoria = produto.categoria
            quantidade = produto.quantidade
            if quantidade < self.ESTOQUE_MINIMO.get(categoria, 0):
                print(f"Estoque baixo para a categoria {categoria}: {quantidade} unidades (mínimo permitido: {self.ESTOQUE_MINIMO[categoria]})")
            elif quantidade > self.ESTOQUE_MAXIMO.get(categoria, 0):
                print(f"Estoque excedido para a categoria {categoria}: {quantidade} unidades (máximo permitido: {self.ESTOQUE_MAXIMO[categoria]})")

    




