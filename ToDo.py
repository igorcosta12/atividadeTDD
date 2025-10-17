class TodoList:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, nome, descricao):
        self.tarefas.append({"nome": nome, "descricao": descricao, "status": "pendente"})

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["status"] = "concluída"
        else:
            print("Índice inválido!")

    def marcar_andamento(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["status"] = "em andamento"
        else:
            print("Índice inválido!")

    def editar(self, indice, novo_nome, nova_descricao):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["nome"] = novo_nome
            self.tarefas[indice]["descricao"] = nova_descricao
        else:
            print("Índice inválido!")

    def excluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
        else:
            print("Índice inválido!")

    def listar(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            print("\n===== LISTA DE TAREFAS =====")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i} - {tarefa['nome']} | {tarefa['descricao']} | Status: {tarefa['status']}")


def exibir_menu():
    print("\n===== SISTEMA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar como CONCLUÍDA")
    print("4 - Marcar como EM ANDAMENTO")
    print("5 - Editar tarefa")
    print("6 - Excluir tarefa")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    todo = TodoList()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            todo.adicionar(nome, descricao)
            print("Tarefa adicionada!")

        elif opcao == "2":
            todo.listar()

        elif opcao == "3":
            todo.listar()
            indice = int(input("Digite o número da tarefa para marcar como concluída: "))
            todo.marcar_concluida(indice)

        elif opcao == "4":
            todo.listar()
            indice = int(input("Digite o número da tarefa para marcar como em andamento: "))
            todo.marcar_andamento(indice)

        elif opcao == "5":
            todo.listar()
            indice = int(input("Digite o número da tarefa para editar: "))
            novo_nome = input("Novo nome: ")
            nova_desc = input("Nova descrição: ")
            todo.editar(indice, novo_nome, nova_desc)

        elif opcao == "6":
            todo.listar()
            indice = int(input("Digite o número da tarefa para excluir: "))
            todo.excluir(indice)
            print("Tarefa excluída!")

        elif opcao == "0":
            print("Saindo... Valeu!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
