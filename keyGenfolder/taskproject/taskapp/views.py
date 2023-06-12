from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,"base.html",{'key':'..'})

def keyg(request):
    if request.method == 'POST':
        ln = request.POST['dd']
        typ=request.POST['character']
        ln=int(ln)
        char = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numm=list('1234567890')
        mix=list('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        key = ''
        if typ == 'ch':
            for x in range(ln):
                key += random.choice(char)
            return render(request, "base.html", {'key': key})
        elif typ == 'nm':
            for x in range(ln):
                key += random.choice(numm)
            return render(request, "base.html", {'key': key})
        else:
            for x in range(ln):
                key += random.choice(mix)
            return render(request, "base.html", {'key': key})


