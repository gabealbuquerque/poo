from livro import Livro, Usuario

def test_livro():
    livro = Livro('Le Petit Prince', ['Antoine De Saint-Exupéry'], True)
    
    assert livro.titulo == 'Le Petit Prince'
    assert livro.autores == ['Antoine De Saint-Exupéry']
    assert livro.get_disponivel() is True

def test_emprestimo_e_devolucao():
    livro = Livro('Le Petit Prince', ['Antoine De Saint-Exupéry'], True)
    usuario = Usuario('João', [livro])

    usuario.emprestar(livro)
    assert livro.get_disponivel() is False

    usuario.devolver(livro)
    assert livro.get_disponivel() is True