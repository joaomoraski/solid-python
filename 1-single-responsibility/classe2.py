class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'Pessoa(nome={self.nome})'


class PessoaBD:
    def salvar(self, pessoa):
        print(f'Pessoa: {pessoa} salva no banco de dados')


if __name__ == '__main__':
    p = Pessoa('Jão Moraski')
    db = PessoaBD()
    db.salvar(p)
