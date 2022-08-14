from django.urls import path
from . import views

app_name = 'KOPPEE'
urlpatterns = [
    path('', views.job_list),
    path('<str:slug>',views.job_detail,name='job_detail'),
]
