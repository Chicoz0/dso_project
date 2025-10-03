from controllers.abstract_user_controller import AbstractUserController

class AdminController(AbstractUserController):
    def __init__(self):
        admins = []
    
    def delete_user(self, user_login):
        pass  #aceita qlq login

    def suspend_user(self, user_login):
        pass #troca o "status" do usuario pra "suspended" - ele n pode fazer acoes de Conexao nem de Confirmacao

    # vamos dar acesso ao admin pra controalr controladores de evento, confirmacao de evento e conexão?