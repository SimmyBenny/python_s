from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place
from . models import staff

# Create your views here.
def index(request):
   obj=place.objects.all()
   obj1 = staff.objects.all()
   return render(request,"index.html",{'key':obj,'key1':obj1})

# def dst(request):
#    obj = place.objects.all()
#    if request.method == 'get':
#       place=request.GET['place']
#       for row in obj:
#          if obj.name == place:
#             return redirect('destinations.html')
#       else:
#          key='This package doesnt exist'
#          return redirect('destinations.html',{'key':key})
