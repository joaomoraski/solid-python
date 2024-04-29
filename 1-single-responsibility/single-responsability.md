# Single Responsibility Principle (SRP)


Basicamente é o princípio que diz que toda classe, método e função só deve existir uma razão para que seja alterada.


Os propósitos desse princípio são
- Criar classes, funções e métodos mais coesos e robustos
- Promover uma composição de classe melhor
- Evitar duplicidade de código


### Vamos começar analisando a classe do arquivo classe1.py
Obs: No arquivo .py é possível achar alguns comentários, aproveitei para aprender python
devido a uma nova oportunidade de trabalho que estarei começando logo logo, então algumas coisas eu fiz comentarios para
fins de estudo mesmo.
```python
class Pessoa:
   def __init__(self, nome):
       self.nome = nome


   def __repr__(self):
       return f'Pessoa(nome={self.nome})'


   @classmethod
   def salvar(cls, pessoa):
       print(f'Pessoa: {pessoa} salva no banco de dados')


if __name__ == '__main__':
   p = Pessoa('Jão Moraski')
   Pessoa.salvar(p)
```


Essa classe possui duas responsabilidades atribuídas a ela:
1. Controlar as propriedades da pessoa;
2. Salvar a entidade no banco de dados.<br>


Caso, futuramente você queira salvar a pessoa em outro lugar, banco ou etc você provavelmente precisaria alterar o método save.<br>
E isso provavelmente iria alterar a classe inteira também.


### Considerando o SRP
Precisamos recriar a classe para que ela seja separada em duas classes.<br>
Vamos analisar o arquivo classe2.py
```python
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
```


Para este caso, se você quiser alterar a função de salvar para que seja trocado o lugar de armazenamento ou algo do tipo
É só criar outra função no PessoaBD.


### Bonus
Arquivo: classe3.py<br>
Para tornar mais conveniente podemos usar Pessoa como fachada para acessar PessoaDB.
```python
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
```


Com esse texto conseguimos ter uma base sobre como funciona o SRP, considerando que uma classe, método ou função tenha
apenas uma razão para ser alterada.