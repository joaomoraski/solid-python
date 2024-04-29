# Open-closed Principle


Basicamente é o princípio que diz que toda classe, método e função deve ser aberta para expansão, porém fechada para modificações.


Apesar de soar um pouco contraditório, ele tem um propósito de tornar fácil a adição de novas features ou use cases para o sistema
sem diretamente alterar o código existente.


### Vamos começar analisando a classe do arquivo classe1.py
```python
class Person:
   def __init__(self, name):
       self.name = name


   def __repr__(self):
       return f'Person(name={self.name})'




class PersonStorage:
   def save_to_database(self, person):
       print(f'Save the {person} to database')


   def save_to_json(self, person):
       print(f'Save the {person} to a JSON file')


if __name__ == '__main__':
   person = Person('Jão Moraski')
   storage = PersonStorage()
   storage.save_to_database(person)
```


Neste caso, a classe PersonStorage tem dois métodos, save_to_database() e save_to_json().<br>
Futuramente, se por acaso fosse necessário salvar Person como um arquivo XML, você precisa alterar a classe PersonStorage.<br>
Isso significa que a classe de PersonStorage não é aberta a extensão, e sim a modificação. Violando o princípio de open-closed


### Considerando o princípio
Para alterarmos a lógica da classe para ser possível se encaixar no princípio de open-closed, seria necessário alterar
o estilo da classe para que fosse uma classe abstrata com o método de salvar e ela ser implementada em outras classes.


```python
from abc import ABC, abstractmethod




class Person:
   def __init__(self, name):
       self.name = name


   def __repr__(self):
       return f'Person(name={self.name})'




class PersonStorage(ABC):
   @abstractmethod
   def save(self, person):
       pass




class PersonDB(PersonStorage):
   def save(self, person):
       print(f'Save the {person} to database')




class PersonJSON(PersonStorage):
   def save(self, person):
       print(f'Save the {person} to a JSON file')




class PersonXML(PersonStorage):
   def save(self, person):
       print(f'Save the {person} to an XML file')




if __name__ == '__main__':
   person = Person('John Doe')
   storage = PersonXML()
   storage.save(person)
```


Basicamente no código acima é feito a criação da classe abstrata PersonStorage, que é herdada nas outras classes para
indicar onde a pessoa vai ser salva, por exemplo, no PersonXML().