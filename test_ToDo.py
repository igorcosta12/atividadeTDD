import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_adicionar_tarefa(self):
        self.todo.adicionar("Estudar", "Estudar TDD em Python")
        self.assertEqual(len(self.todo.tarefas), 1)
        self.assertEqual(self.todo.tarefas[0]["nome"], "Estudar")

    def test_marcar_como_concluida(self):
        self.todo.adicionar("Ler", "Ler um livro")
        self.todo.marcar_concluida(0)
        self.assertEqual(self.todo.tarefas[0]["status"], "concluída")

    def test_marcar_como_andamento(self):
        self.todo.adicionar("Treinar", "Ir para academia")
        self.todo.marcar_andamento(0)
        self.assertEqual(self.todo.tarefas[0]["status"], "em andamento")

    def test_editar_tarefa(self):
        self.todo.adicionar("Dormir", "Dormir cedo")
        self.todo.editar(0, "Dormir muito", "Dormir cedo e bem")
        self.assertEqual(self.todo.tarefas[0]["nome"], "Dormir muito")

    def test_excluir_tarefa(self):
        self.todo.adicionar("Jogar", "Jogar videogame")
        self.todo.excluir(0)
        self.assertEqual(len(self.todo.tarefas), 0)

if __name__ == "__main__":
    unittest.main()
