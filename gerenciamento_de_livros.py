livros = {
    "pequeno principe" : {"autor": "Dante" , "quantidade": 10},
    "pequeno rei" : {"autor": "Dante" , "quantidade": 13},
    "pequeno soldado" : {"autor": "Dante" , "quantidade": 100}
}

emprestimo = []

def obter_livro(livros):
    nome = input("nome do livro: ").lower().strip()
    autor = input("nome do autor: ")
    quantidade = int(input("quantidade de exemplares: "))
    if nome not in livros:
        livros[nome] = {"autor": autor, "quantidade": quantidade}
    else:
        print("livro já existe")

def listar_livros(livros):
    if not livros:
        print("nenhum livro cadastrado no sistema")
    else:
        resultado = ["listrar livros"]
        for chave, valor in sorted(livros.items(), key=lambda item: item[0]):
            autor = valor["autor"]
            quantidade = valor["quantidade"]
            resultado.append(f"({chave}: {autor} - {quantidade})")
        print("\n".join(resultado))

    
def remover_livro(livros):
    nome = input("nome do livro: ").lower().strip()
    if nome in livros:
        del livros[nome]
        print(f"Livro '{nome}' removida com sucesso!")
    else:
        print("Erro: livro não encontrado")



def atualizar_quantidade(livros):
    nome = input("nome do livro: ").lower().strip()
    quantidade = int(input("quantidade nova: "))
    if nome in livros:
        livros[nome]["quantidade"] = quantidade
        print(f"Quantidade de '{nome}', atualizada para '{quantidade}'")
    else:
        print("Erro: livro não cadastrado")


def exibir_menu():
    opcoes = ["Adicionar livro", "Listar livros", "Remover livro", "Atualizar quantidade de livros", "Registrar empréstimo", "Exibir histórico de empréstimos", "Sair"]
    print("Menu do gerenciador")
    print("\n".join([f"{i+1}. {op}" for i, op in enumerate(opcoes)]))
    return opcoes


def registrar_emprestimo(livros):
    nome = input("nome do livro: ").lower()
    quantidade = int(input("quantidade de livros para emprestimo: "))
    if nome in livros:
        if livros[nome]["quantidade"] >= quantidade:
            livros[nome]["quantidade"] -= quantidade
            emprestimo.append(f"{nome} - {quantidade}")
            print("emprestimo realizado com sucesso")
        else:
            print(f"Não foi possivel realizar o emprestimo por conta da quantidade disponivel\ntemos {livros[nome]["quantidade"]} livros disponiveis")
    else:
        print("Erro: livro não cadastrado")            


def mostrar_historico(emprestimo):
    print(f"Historico de emprestimo:\n{emprestimo}")


def main():
    while True:
        exibir_menu()
        
        escolha = input("escolha uma das funções: ")
        
        if escolha == "1":
            obter_livro(livros)
        elif escolha == "2":
            listar_livros(livros)
        elif escolha == "3":
            remover_livro(livros)
        elif escolha == "4":
            atualizar_quantidade(livros)
        elif escolha == "5":
            registrar_emprestimo(livros)
        elif escolha == "6":
            mostrar_historico(emprestimo)
        elif escolha == "7":
            break
        else:
            print("opção invalida")

main()
