from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    url(r'^edit_worked_time/(?P<task_id>\w+)/$', views.edit_worked_time, name="edit_worked_time"),
    path(r'^add_worked_time/$', views.add_worked_time, name="add_worked_time")        
]
