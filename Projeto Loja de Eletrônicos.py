# Sistema de Controle de Estoque para Loja de Eletrônicos

estoque = [] # Lista para armazenar os produtos como dicionários


# Função para adicionar um novo produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    # Verifica se o produto já existe
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print("Produto já existe no estoque.")
            return
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro: Preço ou quantidade inválida.")


# Função para atualizar um produto
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ").strip()
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            try:
                novo_preco = float(input("Novo preço: R$ "))
                nova_quantidade = int(input("Nova quantidade em estoque: "))
                produto["preco"] = novo_preco
                produto["quantidade"] = nova_quantidade
                print(f"Produto '{nome}' atualizado com sucesso!")
                return
            except ValueError:
                print("Erro: Preço ou quantidade inválida.")
                return
    print("Produto não encontrado.")


# Função para excluir um produto
def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ").strip()
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print(f"Produto '{nome}' excluído com sucesso!")
            return
    print("Produto não encontrado.")


# Função para visualizar o estoque
def visualizar_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\nEstoque Atual:")
        print("-" * 40)
        for produto in estoque:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']} unidades")
            print("-" * 40)


# Função para exibir o menu e capturar a escolha do usuário
def menu():
    while True:
        print("\n--- Sistema de Controle de Estoque ---")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Excluir produto")
        print("4. Visualizar estoque")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do sistema
menu()
