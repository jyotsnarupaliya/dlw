
from datetime import datetime, time, timedelta
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import template

from .forms import NameForm
from .forms import ContingentForm
from .models import employee
# Create your views here.

def index(request):
    index_template = template.loader.get_template('ta/index.html')
    return HttpResponse(index_template.render({}, request))


def ta_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']
            s_train_no = form.cleaned_data['s_train_no']
            s_date = form.cleaned_data['s_date']
            s_time = form.cleaned_data['s_time']
            return_train_no = form.cleaned_data['return_train_no']
            f_date = form.cleaned_data['f_date']
            f_time = form.cleaned_data['f_time']

            employees = employee.objects.filter(emp_no=emp_id)
            basic_ta = employees[0].ta
            branch = employees[0].branch
            emp_name = employees[0].emp_name
            headq = employees[0].headq
            branch = employees[0].branch
            basic_pay = employees[0].basic_pay
            division = employees[0].division
            
            final_ta = calculate(emp_id, s_date, s_time, f_date, f_time)
            days = (f_date - s_date).days
            context = {
                'emp_id': emp_id, 
                's_train_no': s_train_no,
                's_date': s_date,
                's_time': s_time,
                'f_date': f_date,
                'f_time': f_time,
                'basic_ta': basic_ta,
                'final_ta': final_ta,
                'branch': branch,
                'emp_name': emp_name,
                'headq': headq,
                'basic_pay': basic_pay,
                'division': division,
                'return_train_no': return_train_no,
                'days': days
                }

            result_template = template.loader.get_template('ta/result.html')
            return HttpResponse(result_template.render(context, request))
    else:
        form = NameForm()
    
    context = {'form': form}
    ta_template = template.loader.get_template('ta/ta_form.html')
    return HttpResponse(ta_template.render(context, request))


def contingent_form(request):
    if request.method == 'POST':
        form = ContingentForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']
            reached_date = form.cleaned_data['reached_date']
            return_date = form.cleaned_data['return_date']
            kms = form.cleaned_data['kms']
            rate = form.cleaned_data['rate']

            days = (return_date - reached_date).days
            contingent = kms * rate * days

            employees = employee.objects.filter(emp_no=emp_id)
            branch = employees[0].branch
            emp_name = employees[0].emp_name
            headq = employees[0].headq
            branch = employees[0].branch
            basic_pay = employees[0].basic_pay
            division = employees[0].division

            context = {
            'emp_id': emp_id,
            'reached_date': reached_date,
            'return_date': return_date,
            'kms': kms,
            'rate': rate,
            'days': days,
            'contingent': contingent,
            'branch': branch,
            'emp_name': emp_name,
            'headq': headq,
            'basic_pay': basic_pay,
            'division': division,
            }

            contingent_result_template = template.loader.get_template('ta/contingent_result.html')
            return HttpResponse(contingent_result_template.render(context, request))

    else:
        form = ContingentForm()

    context = {'form': form}
    contingent_template = template.loader.get_template('ta/contingent_form.html')
    return HttpResponse(contingent_template.render(context, request))

def calculate(e_id, s_date, s_time, f_date, f_time):
    employees = employee.objects.filter(emp_no=e_id)
    basic_ta = employees[0].ta
    final_ta = 0

    #import ipdb; ipdb.set_trace()

    datetime_midnight = datetime.combine(datetime.today(), time(hour=22))
    datetime_start = datetime.combine(datetime.today(), s_time)
    datetime_finish = datetime.combine(datetime.today(), f_time)
    diff_time = timedelta(seconds=12*3600)

    if diff_time <= (datetime_midnight - datetime_start):
        final_ta = basic_ta
    else:
        final_ta = 0.7 * basic_ta

    days = (f_date - s_date).days
    final_ta = final_ta + basic_ta * days

    if diff_time  <= (datetime_midnight - datetime_finish):
        final_ta = final_ta + basic_ta
    else:
        final_ta = final_ta + 0.7 * basic_ta

    return final_ta