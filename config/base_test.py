from services.users.api_users import UsersAPI

class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
