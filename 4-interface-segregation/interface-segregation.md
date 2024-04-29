# Interface Segregation Principle (ISP)


Na programação orientada a objetos criamos interfaces para serem uma coleção de métodos que um objeto precisa ter.<br>
O objetivo da interface é garantir que os clientes solicitem corretamente os métodos do objeto pela interface.


No python é usado classes abstratas para implementar interfaces por conta do <i>duck typing principle</i>, que diz:<br>


```
se anda igual um pato e faz quack igual a um pato, deve ser um pato
```


Em outras palavras, os métodos de uma classe determinam o que os objetos vão ser, e não o tipo da classe.


### Vamos começar analisando a interface do arquivo classe1.py


```python
from abc import ABC, abstractmethod




class Vehicle(ABC):
   @abstractmethod
   def go(self):
       pass


   @abstractmethod
   def fly(self):
       pass
```


A classe abstrata de veículo possui dois métodos, go() e fly(), que seriam as ações de um veículo, porém, no caso abaixo
por exemplo, nós iremos ter um problema


```python
class Aircraft(Vehicle):
   def go(self):
       print("Taxiing")


   def fly(self):
       print("Flying")




class Car(Vehicle):
   def go(self):
       print("Going")


   def fly(self):
       raise Exception('The car cannot fly')
```


É notável que carro não tem a função fly(), e nesse caso ele seria forçado a implementar o fly() com uma Exception,
e nesse caso ele também não seria usado.<br>
Isso viola o princípio de ISP


### Como resolver isso.


Arquivo: classe2.py


```python
from abc import ABC, abstractmethod




class Movable(ABC):
   @abstractmethod
   def go(self):
       pass




class Flyable(Movable):
   @abstractmethod
   def fly(self):
       pass




class Aircraft(Flyable):
   def go(self):
       print("Taxiing")


   def fly(self):
       print("Flying")




class Car(Movable):
   def go(self):
       print("Going")
```


Dessa forma garantimos que a interface tem apenas um método, faz apenas uma coisa que é preciso fazer, e garantimos que
seja possível usa-la em outros casos sem violar o princípio, por exemplo, agora carro usa apenas o Moveable e não precisa
lançar uma Exception por conta do Fly()