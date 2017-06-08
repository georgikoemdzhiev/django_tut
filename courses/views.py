# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from __future__ import unicode_literals

from django.shortcuts import render

from . models import Course
# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render(request,
                  'courses/course_list.html',
                  {'courses': courses} )

def my_method(request):
    courses = Course.objects.all()
    return render(request, 'courses/my.html', {'courses':courses})
