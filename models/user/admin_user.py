from models.user.base_user import BaseUser
from models.user.user import User

class AdminUser(BaseUser):
    def __init__(self, username: str, password: str, email: str):
        super().__init__(username, password, email)
    
    # Inativa ou ativa uma conta de usuário
    def change_user_status(self, user: User, new_status: bool):
        return user.status(new_status)
