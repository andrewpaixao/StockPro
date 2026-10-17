produtos = [
    {"Nome": "Mouse gamer", "Preço": 89.90, "Quantidade": 10},
    {"Nome": "Teclado mecânico", "Preço": 199.90, "Quantidade": 8},
    {"Nome": "Monitor 24''", "Preço": 899.90, "Quantidade": 5},
    {"Nome": "Fone de ouvido", "Preço": 59.90, "Quantidade": 20}
]

def atualizar_produtos():
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["Nome"].lower() == nome.lower():
            print(f"Produto encontrado: {produto['Nome']}\n Quantidade atual do produto é: {produto['Quantidade']}")

            quantidade = int(
                input("Quantas unidades deseja adicionar ao estoque?")
            )
            if quantidade > 0:
                produto["Quantidade"] += quantidade
                print(f"\n Estoque atualizado com sucesso!")
                print(f"Nova quantidade do produto {produto['Nome']}: {produto['Quantidade']}")
            else:
                print("Digite uma quantidade maior que zero para atualizar o estoque.")

            return
        print("Produto não encontrado no estoque.")
while True:
    print("""\n---MENU DE OPÇÕES---\n
    ESTOQUE DE PRODUTOS""")
    print("1- Listar produtos")
    print("2- Adicionar produto")
    print("3- Atualizar estoque")
    print("4- Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\n---LISTA DE PRODUTOS---")
        print("Nome do produto | Preço | Quantidade")
        valor_total_geral = 0
        for produto in produtos:
            valor_total_geral += produto["Preço"] * produto["Quantidade"]
            print(
                f"{produto['Nome']} | R$ {produto['Preço']:.2f} "
                f"| {produto['Quantidade']}"
            )
            if produto["Quantidade"] <= 5:
                print(
                    f"Estoque baixo do produto: {produto['Nome']}. "
                    "Faça um novo pedido para repor o estoque."
                )
        print(f"Valor total do estoque: R$ {valor_total_geral:.2f}")

    elif opcao == "2":
        print("\n---ADICIONAR PRODUTO---")
        novo_produto = {
            "Nome": input("Digite o nome do produto: "),
            "Preço": float(input("Digite o preço do produto: ")),
            "Quantidade": int(input("Digite a quantidade do produto: "))
        }
        produtos.append(novo_produto)
        print(f"Produto '{novo_produto['Nome']}' adicionado com sucesso!")
    elif opcao == "3":
        atualizar_produtos()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Digite uma opção válida.")