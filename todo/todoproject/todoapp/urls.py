from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:tid>/',views.delete,name='delete'),
    path('update/<int:tid>/',views.update,name='update'),
    path('tv/',views.Taskview.as_view(),name='tv'),
    path('taskdview/<int:pk>',views.taskdview.as_view(),name='taskdview'),
    path('taskupview/<int:pk>',views.taskupview.as_view(),name='taskupview'),
    path('taskdelete/<int:pk>',views.taskdelete.as_view(),name='taskdelete'),

]