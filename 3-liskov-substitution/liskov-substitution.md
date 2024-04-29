# Liskov Substitution Principle (LSP)


Basicamente é o princípio que diz que toda classe filha, deve ser capaz de ser substituída por sua classe pai, sem causar erros.<br>
Ele foca em garantir que a classe filha possa assumir o papel da classe pai sem causar problemas.


### Vamos começar analisando a classe do arquivo classe1.py
```python
from abc import ABC, abstractmethod


class Notification(ABC):
   @abstractmethod
   def notify(self, message, email):
       pass


class Email(Notification):
   def notify(self, message, email):
       print(f'Send {message} to {email}')


class SMS(Notification):
   def notify(self, message, phone):
       print(f'Send {message} to {phone}')


if __name__ == '__main__':
   notification = SMS()
   notification.notify('Ola', 'joao@moraski.com')
```


Neste caso, temos 3 classes, uma classe abstrata chamada Notificação, uma classe chamada Email e uma chamada SMS.<br>
Porém, como é visto na chamada da Main, se você instâncias notificação como um SMS() e passar um email para o contato ele vai continuar
"funcionando" normal, obviamente nesse caso, ele iria passar o email como um parâmetro para o número de telefone.


### Como resolver isso.
Primeiro, precisamos fazer com que o método notify da classe abstrata não receba mais email como parâmetro.
```python
from abc import ABC, abstractmethod


class Notification(ABC):
   @abstractmethod
   def notify(self, message):
       pass
```
Depois disso, precisamos implementar o campo de email e número de telefone no construtor das outras classes.
```python
class Email(Notification):
   def __init__(self, email):
       self.email = email
  
   def notify(self, message):
       print(f'Send {message} to {self.email}')


class SMS(Notification):
   def __init__(self, phone):
       self.phone = phone
  
   def notify(self, message):
       print(f'Send {message} to {self.phone}')
```
Agora podemos implementar uma classe geral para as notificações chamada NotificationManager e então fazer ela mandar as notificações
```python
from abc import ABC, abstractmethod


class Notification(ABC):
   @abstractmethod
   def notify(self, message):
       pass


class Email(Notification):
   def __init__(self, email):
       self.email = email


   def notify(self, message):
       print(f'Send "{message}" to {self.email}')


class SMS(Notification):
   def __init__(self, phone):
       self.phone = phone


   def notify(self, message):
       print(f'Send "{message}" to {self.phone}')


class Contact:
   def __init__(self, name, email, phone):
       self.name = name
       self.email = email
       self.phone = phone


class NotificationManager:
   def __init__(self, notification):
       self.notification = notification


   def send(self, message):
       self.notification.notify(message)


if __name__ == '__main__':
   contact = Contact('Jão Moraski', 'joao@moraski.com', '+55 (44) 99991-8888')


   sms_notification = SMS(contact.phone)
   email_notification = Email(contact.email)


   notification_manager = NotificationManager(sms_notification)
   notification_manager.send('Olá Jão')


   notification_manager.notification = email_notification
   notification_manager.send('Oi João')
```
Assim, garantimos que a classe filha pode ser substituída por sua classe pai e continuar a funcionar.