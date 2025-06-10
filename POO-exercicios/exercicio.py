class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print("Livro nao disponivel, foi emprestado com sucesso!")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            print("Livro ja esta disponivel, foi devolvido com sucesso!")
        self.disponivel = True

    def obter_info(self):
        return f"Título do livro: {self.titulo} | Ano de publicação: {self.ano_publicacao}| Disponivel: {self.disponivel}"


class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                print(f"livro {livro.titulo} nao disponivel")
                return False
        return True


colecao = ColecaoLivros("Colecao1", 2010, True)
colecao.adicionar_livro(ItemBiblioteca("a", 2015, True))
colecao.adicionar_livro(ItemBiblioteca("abc", 2025, False))
colecao.adicionar_livro(ItemBiblioteca("hsajkfsdhf", 2115, False))

colecao.verificar_disponibilidade_colecao()