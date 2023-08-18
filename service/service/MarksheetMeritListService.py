from .BaseService import BaseService
from service.models import Marksheet
from django.core.paginator import Paginator,InvalidPage
from django.db.models import Q,ExpressionWrapper,F,DecimalField


'''
It contains Marksheet Merit business logics.   
'''
class MarksheetMeritListService(BaseService):

    def get_model(self):
        return Marksheet

def get_table(db_model_class, ordered_paramter, page=1, pzsz=3):
    totalMarks = ExpressionWrapper(F('physics')+F('chemistry')+F('maths'),output_field=DecimalField())
    percentage = ExpressionWrapper(F('totalMarks')/3,output_field=DecimalField())
    qs_of_contents = db_model_class.objects.annotate(totalMarks=totalMarks,
                                                    percentage=percentage).order_by(ordered_paramter)
    paginator = Paginator(qs_of_contents, pzsz)
    last_page_no = int(paginator.num_pages)

    try:
        table_of_contents = paginator.page(int(page))

    except InvalidPage:
        # if we exceed the page limit we return the last page
        table_of_contents = paginator.page(paginator.num_pages)

    return table_of_contents, last_page_no