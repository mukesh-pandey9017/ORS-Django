from service.models import User
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.core.paginator import Paginator,InvalidPage
from django.db.models import Q


'''
It contains User business logics.   
'''

class UserService(BaseService):
    def authenticate(self, params={}):
        userList = self.search(params)
        if (userList.count() == 1):
            return userList[0]
        else:
            return None


    def search(self, params):

        q = self.get_model().objects.filter()

        val = params.get("login_id", None)
        if(DataValidator.isNotNull(val)):
            q = q.filter(login_id=val)

        val = params.get("password", None)
        if(DataValidator.isNotNull(val)):
            q = q.filter(password=val)
        return q

    def get_model(self):
        return User


def get_table(db_model_class, ordered_paramter, page=1, pzsz=3, filter_param=''):
    if filter_param != "":

        qs_of_contents = db_model_class.objects.all().filter(
            Q(login_id__icontains=filter_param) |
            Q(firstName__icontains=filter_param) |
            Q(lastName__icontains=filter_param) |
            Q(role_Name__icontains=filter_param))
        print(qs_of_contents)
    else:
        qs_of_contents = db_model_class.objects.all().order_by(ordered_paramter)  # filter(id__in=ids)#

    paginator = Paginator(qs_of_contents, pzsz)
    last_page_no = int(paginator.num_pages)

    try:
        table_of_contents = paginator.page(int(page))

    except InvalidPage:
        # if we exceed the page limit we return the last page
        table_of_contents = paginator.page(paginator.num_pages)

    return table_of_contents, last_page_no

