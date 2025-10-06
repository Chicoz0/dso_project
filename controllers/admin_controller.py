from models.user.admin_user import AdminUser
from controllers.user_controller import UserController
from views.login_view import LoginView
from views.register_view import RegisterView
from views.logged_user_view import LoggedUserView

class AdminController:
    def __init__(self):
        self.__admins = []

    @property
    def admins(self):
        return self.__admins
    
    def change_user_status(self, target_user_id: str, new_status: bool):
        if UserController.find_user_by_id(target_user_id) != None:
            AdminUser.change_user_status(target_user_id, new_status)
        else:
            return  #ta errado, sei la