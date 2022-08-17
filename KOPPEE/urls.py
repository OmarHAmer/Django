from django.urls import path
from . import views ,api

app_name = 'KOPPEE'
urlpatterns = [
    path('', views.job_list,name = 'home'),
    path('api/list', api.jobapi,name = 'jobapi'),
    path('<str:slug>',views.job_detail,name='job_detail'),
]
