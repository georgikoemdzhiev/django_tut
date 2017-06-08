# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, Step


class StepInline(admin.StackedInline):
    model = Step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]
# Register a model to appear in the admin's pannel
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)
