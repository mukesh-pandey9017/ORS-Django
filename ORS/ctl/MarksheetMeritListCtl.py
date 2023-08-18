from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from service.service.MarksheetMeritListService import MarksheetMeritListService,get_table


class MarksheetMeritListCtl(BaseCtl):

    def request_to_form(self, requestform):
        self.form['page_num'] = requestform.getlist('curr_pg_no')

    def display(self, request, params={}):
        self.form['index'] = 1
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='-percentage',
                                       pzsz=self.pg_size)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def next(self, request, params={}):
        nextPageNo = int((self.form['page_num'])[0]) + 1
        self.form['index'] = ((nextPageNo - 1) * self.pg_size) + 1
        # srch_prm = self.form["srch_prm"]
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='-percentage',
                                       page=nextPageNo,
                                       pzsz=self.pg_size)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def previous(self, request, params={}):
        prevPageNo = int((self.form['page_num'])[0]) - 1
        self.form['index'] = ((prevPageNo - 1) * self.pg_size) + 1
        # srch_prm = self.form["srch_prm"]
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='-percentage',
                                       page=prevPageNo,
                                       pzsz=self.pg_size)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def submit(self, request, params={}):
        pass

    def get_template(self):
        return "MarksheetMeritList.html"

    # Service of Role
    def get_service(self):
        return MarksheetMeritListService()


    #     self.form['rollNumber'] = requestForm.get('rollNumber', None)
    #     self.form['name'] = requestForm.get('name', None)
    #     self.form['physics'] = requestForm.get('physics', None)
    #     self.form['chemistry'] = requestForm.get('chemistry', None)
    #     self.form['maths'] = requestForm.get('maths', None)
    #     self.form['ids'] = requestForm.getlist('ids', None)
    #
    #
    # #Display Marksheet page
    # def display(self,request,params={}):
    #     record = self.get_service().search(self.form)
    #     self.page_list = record['data']
    #     res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
    #     return res
    #
    #
    # # Submit Marksheet page
    #
    # def submit(self,request,params={}):
    #     record = self.get_service().search(self.form)
    #     self.page_list = record['data']
    #     if self.page_list==[]:
    #         self.form['mesg'] = 'No record found'
    #     res = render(request,self.get_template(),{'form':self.form,'pageList':self.page_list})
    #     return res
        
    # Template html of Role page    
