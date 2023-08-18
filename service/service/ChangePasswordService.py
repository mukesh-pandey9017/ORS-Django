from service.models import User
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService

'''
It contains user business logics.
'''

class ChangePasswordService(BaseService):

    def authenticate(self, params={}):
        userList = self.search2(params)
        if (userList.count() == 1):
            return userList[0]
        else:
            return None

    def search2(self, params):

        q = self.get_model().objects.filter()

        val = params.get("login_id", None)
        if (DataValidator.isNotNull(val)):
            q = q.filter(login_id=val)

        val = params.get("password", None)
        if (DataValidator.isNotNull(val)):
            q = q.filter(password=val)

        return q

    def get_model(self):
        return User
