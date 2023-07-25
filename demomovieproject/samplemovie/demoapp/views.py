from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForms
from .models import Movies


def index(request):
    movie = Movies.objects.all()
    context = {'movie_list': movie}
    return render(request,'index.html',context)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    context1={'movie': movie}
    return render(request,"detail.html",context1)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movies(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')
def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MovieForms(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
