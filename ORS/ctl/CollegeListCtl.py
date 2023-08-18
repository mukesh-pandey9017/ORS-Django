from .BaseCtl import BaseCtl
from django.shortcuts import render
from service.service.CollegeService import CollegeService,get_table


class CollegeListCtl(BaseCtl):

    def request_to_form(self, requestform):
        self.form['srch_prm'] = requestform.get("srch_prm", None)
        self.form['ids'] = requestform.getlist("ids", None)
        self.form['page_num'] = requestform.getlist('curr_pg_no')

    def display(self, request, params={}):
        self.form['index'] = 1
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='id',
                                       pzsz=self.pg_size)
        res = render(request, self.get_template(), {'pageList': record, "form": self.form})
        return res

    def next(self, request, params={}):
        nextPageNo = int((self.form['page_num'])[0]) + 1
        self.form['index'] = ((nextPageNo - 1) * self.pg_size) + 1
        srch_prm = self.form["srch_prm"]
        record, last_pg_no = get_table(db_model_class=self.get_service().get_model(),
                                       ordered_paramter='id',
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
                                       ordered_paramter='id',
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
                                           ordered_paramter='id',
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
                                           ordered_paramter='id',
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
                                       ordered_paramter='id',
                                       pzsz=self.pg_size,
                                       filter_param=srch_prm)

        if len(record) == 0:
            self.form['msg'] = "No record found"
        res = render(request, self.get_template(), {'pageList': record, 'form': self.form})
        return res

    def get_template(self):
        return "CollegeList.html"

    def get_service(self):
        return CollegeService()
