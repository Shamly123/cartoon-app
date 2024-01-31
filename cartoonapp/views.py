from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cartoon
from .forms import CartoonForm

# Create your views here.


def index(request):
    cartoon=Cartoon.objects.all()
    context={'cartoon_list':cartoon}

    return render(request,"index.html",context)


def detail(request,cartoon_id):
    cartoon=Cartoon.objects.get(id=cartoon_id)
    return render(request,"detail.html",{'x':cartoon})

def add_cartoon(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        cartoon=Cartoon(name=name,desc=desc,year=year,img=img)
        cartoon.save()
    return  render(request,"add.html")


def update(request,id):
    cartoon=Cartoon.objects.get(id=id)
    form=CartoonForm(request.POST or None,request.FILES,instance=cartoon)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'cartoon':cartoon})


def delete(request,id):
    if request.method=='POST':
        cartoon=Cartoon.objects.get(id=id)
        cartoon.delete()
        return redirect('/')

    return render(request,'delete.html')
