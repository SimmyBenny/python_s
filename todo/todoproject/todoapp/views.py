from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import uptask
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView




class Taskview(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'key'

class taskdview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 't1'

class taskupview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'key2'
    fields = ('name','pr','date')

    def get_success_url(self):
        return reverse_lazy('tv')

class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('tv')
# Create your views here.
def index(request):
    task1 = task.objects.all()
    if request.method == 'POST':
        name=request.POST['tname']
        pr=request.POST['prio']
        date=request.POST['date']
        tk=task(name=name,pr=pr,date=date)
        tk.save()

    return render(request,"index.html",{'key':task1})

def delete(request,tid):
    if request.method == 'POST':
        taskn=task.objects.get(id=tid)
        taskn.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,tid):
    tas = task.objects.get(id=tid)
    f = uptask(request.POST or None, instance=tas)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect('/')
    return render(request,'update.html',{'t':tas,'f':f})