# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Exam
from ..util import paginate, get_current_group

def exam_list(request):
    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(group=current_group)
    else:
        exams = Exam.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('subject', 'date', 'teacher', 'group'):
        students = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    return render(request, 'students/exam_list.html',{'exams':exams})

def exam_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exam_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

def exam_delete(request, eid):
    return  HttpResponse('<h1>Delete Exam %s</h1>' % eid)

def exam_result(request, eid):
    return  HttpResponse('<h1>Result Exam %s</h1>' % eid)
