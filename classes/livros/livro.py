class Livro:
    def __init__(self, titulo: str, autores: list, status: bool):
        self.titulo = titulo
        self.autores = autores
        self.__status = status

    def get_disponivel(self):
        return self.__status

    def set_disponivel(self, status: bool):
        self.__status = status


class Usuario:
    def __init__(self, nome: str, livros: list):
        self.nome = nome
        self.livros = livros  # Lista de objetos do tipo Livro

    def emprestar(self, livro: Livro):
        if livro.get_disponivel():
            livro.set_disponivel(False)

    def devolver(self, livro: Livro):
        livro.set_disponivel(True)