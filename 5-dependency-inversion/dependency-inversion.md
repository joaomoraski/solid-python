# Dependency Inversion Principle (ISP)


Este princípio segue as convenções que:


- Módulos de nível alto não devem depender de módulos low-level, ambos devem depender de abstrações
- Abstrações não podem depender de detalhes, detalhes devem depender de abstrações.


### Vamos começar analisando a <i>interface</i> do arquivo classe1.py


```python
class FXConverter:
   def convert(self, from_currency, to_currency, amount):
       print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
       return amount * 1.2




class App:
   def start(self):
       converter = FXConverter()
       converter.convert('EUR', 'USD', 100)




if __name__ == '__main__':
   app = App()
   app.start()
```


Para este caso temos uma Classe FXConverter, que faz a conversão de uma moeda, e a class <i>App</i> e método Start que
instância
FXConverter e mandar a conversão de EUR para USD.<br>
Numa implementação real, FXConverter vai depender de uma API de exchange, e caso essa API caia, ou mude, você precisa
mudar toda a lógica do <i>App</i> também.<br>
Para resolver isso, precisamos inverter as dependências das classes, invés de depender de FXConverter, vamos fazer
as duas dependerem de uma classe em comum.


### Como resolver isso.


Arquivo: classe2.py


```python
from abc import ABC




class CurrencyConverter(ABC):
   def convert(self, from_currency, to_currency, amount) -> float:
       pass




class FXConverter(CurrencyConverter):
   def convert(self, from_currency, to_currency, amount) -> float:
       print('Converting currency using FX API')
       print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
       return amount * 2




class App:
   def __init__(self, converter: CurrencyConverter):
       self.converter = converter


   def start(self):
       self.converter.convert('EUR', 'USD', 100)




if __name__ == '__main__':
   converter = FXConverter()
   app = App(converter)
   app.start()
```


Neste caso, alteramos para que FXConverter dependa da CurrencyConverter, que tem o método de convert. <br>
Fazendo com que <i>App</i> tenha um construtor que precisa ser iniciado com uma instância da classe CurrencyConverter, podemos
fazer com que seja implementada outra classe de converter no futuro de forma mais fácil, por exemplo, ainda no arquivo
classe2,py.


```python
class AlphaConverter(CurrencyConverter):
   def convert(self, from_currency, to_currency, amount) -> float:
       print('Converting currency using Alpha API')
       print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
       return amount * 1.15




if __name__ == '__main__':
   converter = FXConverter()
   app = App(converter)
   app.start()
   converter = AlphaConverter()
   app = App(converter)
   app.start()
```


Assim, podemos trocar a API de exchange sem ter que mudar toda a estrutura do código.