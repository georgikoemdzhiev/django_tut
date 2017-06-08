from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.course_list),
    url(r'^my$', views.my_method),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]
