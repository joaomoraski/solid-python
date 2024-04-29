class Pessoa:

    # Construtor python
    def __init__(self, nome):
        self.nome = nome

    # To string do python
    def __repr__(self):
        return f'Pessoa(nome={self.nome})'

    @classmethod  # Define que é um metodo de classe, agindo na propria classe e nao nas instancias
    # CLS referencia a classe
    def salvar(cls, pessoa):
        print(f'Pessoa: {pessoa} salva no banco de dados')


if __name__ == '__main__':
    p = Pessoa('Jão Moraski')
    Pessoa.salvar(p)
