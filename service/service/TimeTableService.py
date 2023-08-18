from service.models import TimeTable
from .BaseService import BaseService
from django.core.paginator import Paginator,InvalidPage
from django.db.models import Q
'''
It contains TimeTable business logics
'''

class TimeTableService(BaseService):

    def get_model(self):
        return TimeTable


def get_table(db_model_class, ordered_paramter, page=1, pzsz=3, filter_param=''):
    if filter_param != "":

        qs_of_contents = db_model_class.objects.all().filter(
            Q(courseName__icontains=filter_param) |
            Q(subjectName__icontains=filter_param) |
            Q(semester__icontains=filter_param))
        print(qs_of_contents)
    else:
        qs_of_contents = db_model_class.objects.all().order_by(ordered_paramter)

    paginator = Paginator(qs_of_contents, pzsz)
    last_page_no = int(paginator.num_pages)

    try:
        table_of_contents = paginator.page(int(page))

    except InvalidPage:
        # if we exceed the page limit we return the last page
        table_of_contents = paginator.page(paginator.num_pages)

    return table_of_contents, last_page_no