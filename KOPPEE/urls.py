from django.urls import path
from . import views ,api

app_name = 'KOPPEE'
urlpatterns = [
    path('', views.job_list,name = 'home'),
    path('<str:slug>',views.job_detail,name='job_detail'),

    # path('api/list', api.jobapi,name = 'jobapi'),
    # path('api/list/<int:id>', api.job_details,name = 'job_details'),

    path('api/list', api.JobApi.as_view(),name = 'JobApi'),
    path('api/list/<int:id>', api.JobDetails.as_view(),name = 'JobDetails'),

    path('api/listView', views.PostListView.as_view(),name = 'PostListView'),


]
