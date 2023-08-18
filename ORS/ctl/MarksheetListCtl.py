from .BaseCtl import BaseCtl
from django.shortcuts import render
from service.models import Marksheet
from service.service.MarksheetService import MarksheetService, get_table


class MarksheetListCtl(BaseCtl):

    def request_to_form(self,requestform):
        self.form['srch_prm'] = requestform.get("srch_prm", None)
        self.form['ids'] = requestform.getlist("ids", None)
        self.form['page_num'] = requestform.getlist('curr_pg_no')

    def display(self, request, params={}):
        self.form['index'] = 1
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='rollNumber',
                                       pzsz=self.pg_size)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def next(self, request, params={}):
        nextPageNo = int((self.form['page_num'])[0]) + 1
        self.form['index'] = ((nextPageNo - 1) * self.pg_size) + 1
        srch_prm = self.form["srch_prm"]
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='rollNumber',
                                       page=nextPageNo,
                                       pzsz=self.pg_size,
                                       filter_param=srch_prm)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def previous(self, request, params={}):
        prevPageNo = int((self.form['page_num'])[0]) - 1
        self.form['index'] = ((prevPageNo - 1) * self.pg_size) + 1
        srch_prm = self.form["srch_prm"]
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='rollNumber',
                                       page=prevPageNo,
                                       pzsz=self.pg_size,
                                       filter_param=srch_prm)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def deleteRecord(self, request, params={}):
        pageNo = int((self.form['page_num'])[0])
        print('pageno: ', type(pageNo), pageNo)
        self.form['index'] = ((pageNo - 1) * self.pg_size) + 1
        srch_prm = self.form["srch_prm"]
        if (bool(self.form['ids']) == False):
            self.form['error'] = True
            self.form['message'] = "Please Select at least one Checkbox"
            record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                           ordered_paramter='rollNumber',
                                           page=pageNo,
                                           pzsz=self.pg_size,
                                           filter_param=srch_prm)
            res = render(request, self.get_template(), {'pageList': record, "form": self.form})
            return res
        else:
            ids = list(map(int, self.form['ids']))
            self.get_service().get_model().objects.filter(id__in=ids).delete()
            self.form['error'] = False
            self.form['message'] = "DATA HAS BEEN DELETED SUCCESSFULLY"
            record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                           ordered_paramter='rollNumber',
                                           page=pageNo,
                                           pzsz=self.pg_size,
                                           filter_param=srch_prm)
            if last_pg_no < pageNo:
                self.form['index'] = ((last_pg_no - 1) * self.pg_size) + 1

            if len(record) == 0:
                self.form['msg'] = "No record found"

            res = render(request, self.get_template(), {'pageList': record, "form": self.form})
            return res

    def submit(self, request, params={}):
        self.form['index'] = 1
        srch_prm = self.form["srch_prm"]
        print("filter_parameter", srch_prm)
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='rollNumber',
                                       pzsz=self.pg_size,
                                       filter_param=srch_prm)

        if len(record) == 0:
            self.form['msg'] = "No record found"
        res = render(request, self.get_template(), {'pageList': record, 'form': self.form})
        return res

    def get_template(self):
        return "MarksheetList.html"

    # Service of Marksheet
    def get_service(self):
        return MarksheetService()



    #     self.form["rollNumber"]=requestForm.get("rollNumber",None)
    #     self.form["name"]=requestForm.get("name",None)
    #     self.form["physics"]=requestForm.get("physics",None)
    #     self.form["chemistry"]=requestForm.get("chemistry",None)
    #     self.form["maths"]=requestForm.get("maths",None)
    #     self.form["student_ID"]=requestForm.get("student_ID",None)
    #     self.form["ids"]= requestForm.getlist( "ids", None)
    #
    # def display(self,request,params={}):
    #     MarksheetListCtl.count = self.form['pageNo']
    #     record = self.get_service().search(self.form)
    #     self.page_list=record["data"]
    #     self.form['LastId'] = Marksheet.objects.last().id
    #     res = render(request,self.get_template(),{"pageList":self.page_list,'form':self.form})
    #     return res
    #
    #
    # def next(self, request, params={}):
    #     MarksheetListCtl.count+=1
    #     self.form["pageNo"]=MarksheetListCtl.count
    #     record = self.get_service().search(self.form)
    #     self.page_list=record["data"]
    #     self.form['LastId'] = Marksheet.objects.last().id
    #     res = render(request, self.get_template(), {"pageList": self.page_list,"form":self.form})
    #     return res
    #
    # def previous(self, request, params={}):
    #     MarksheetListCtl.count-=1
    #     self.form["pageNo"]=MarksheetListCtl.count
    #     record = self.get_service().search(self.form)
    #     self.page_list=record["data"]
    #     res = render(request, self.get_template(), {"pageList": self.page_list,"form":self.form})
    #     return res
    #
    #
    # def submit(self,request,params={}):
    #     MarksheetListCtl.count = 1
    #     record = self.get_service().search(self.form)
    #     self.page_list=record["data"]
    #     if self.page_list==[]:
    #         self.form['mesg'] = "No record found"
    #     res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
    #     return res
    #
    # def get_template(self):
    #     return "MarksheetList.html"
    #
    # # Service of Marksheet
    # def get_service(self):
    #     return MarksheetService()
    #
    # def deleteRecord(self,request,params={}):
    #     self.form["pageNo"] = MarksheetListCtl.count
    #     if(bool(self.form["ids"])==False):
    #         self.form["error"] = True
    #         self.form["messege"] = "Please Select at least one check box"
    #         record = self.get_service().search(self.form)
    #         self.page_list = record['data']
    #         return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
    #     else:
    #         for ids in self.form["ids"]:
    #             record = self.get_service().search(self.form)
    #             self.page_list=record["data"]
    #
    #             id=int(ids)
    #             if( id > 0):
    #                 r = self.get_service().get(id)
    #                 if r is not None:
    #                     self.get_service().delete(r.id)
    #                     self.form["pageNo"]=1
    #                     record = self.get_service().search(self.form)
    #                     self.page_list=record["data"]
    #                     self.form['LastId'] = Marksheet.objects.last().id
    #                     MarksheetListCtl.count = 1
    #
    #                     self.form["error"] = False
    #                     self.form["messege"] = "DATA IS SUCCESSFULLY DELETED"
    #                     print("ppppppp-->",self.page_list)
    #                     return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
    #                 else:
    #                     self.form["error"] = True
    #                     self.form["messege"] = "Data is not deleted"
    #                     return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
