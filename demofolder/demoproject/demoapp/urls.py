from . import views
from django.urls import path
app_name = 'demoapp'
urlpatterns = [

    path('',views.index,name='index'),

]