from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieupform
# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'movielist':movies
    }
    return render(request,'index.html',context)

def detail(request,mid):
    m=movie.objects.get(id=mid)
    return render(request,"detail.html",{'key':m})

def add(request):
    if request.method == 'POST':
        name=request.POST.get('mname')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['img']
        genre=request.POST['mgen']
        movies=movie(name=name,desc=desc,year=year,img=image,gen=genre)
        movies.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,mid):
    movies=movie.objects.get(id=mid)
    form=movieupform(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'m':movies})

def delete(request,id):
    if request.method == 'POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,"delete.html")