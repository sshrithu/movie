from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Film
from .forms import MovieForm

# Create your views here.
def index(request):
    film=Film.objects.all()
    context={
        'film_list':film
    }
    return render(request,'index.html',context)
def detail(request,film_id):
    film=Film.objects.get(id=film_id)
    return render(request,'detail.html',{'film':film})

def addMovie(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie=Film(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,'add.html')

def editMovie(request,id):
    movie=Film.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def deleteMovie(request,id):
    if request.method=='POST':
        movie=Film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')