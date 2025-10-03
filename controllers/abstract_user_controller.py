from abc import ABC, abstractmethod

class AbstractUserController(ABC):
    def __init__(self):
        pass

    def sign_up_user(self, email: str, login: str, password: str, password_confirmation):
        pass #Testagem e tratamento de excecoes para registro de um user

    def sign_in_user(self, login: str, password: str):
        pass #Testagem e tratamento de excecoes para login

    @abstractmethod    
    def delete_user(self):
        pass #na classe admin vai pegar de input um 'User.login', na classe user n tem input, é ele mesmo

    def change_password(self, password: str, new_password: str,
                        new_password_confirmation: str):
        pass #Testagem e tratamento de excecoes para troca de senha

    def change_email(self, email: str, new_email: str, password: str):
        pass #Testagem e tratamento de excecoes para troca de email