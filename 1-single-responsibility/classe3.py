class PessoaBD:
    def salvar(self, pessoa):
        print(f'Pessoa: {pessoa} salva no banco de dados')


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.db = PessoaBD()

    def __repr__(self):
        return f'Pessoa(nome={self.nome})'

    def salvar(self):
        self.db.salvar(pessoa=self)


if __name__ == '__main__':
    p = Pessoa('Jão Moraski')
    p.salvar()
