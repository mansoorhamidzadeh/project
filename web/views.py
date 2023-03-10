from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def list_view(request):
    objects = Article.objects.all()

    context = {
        'objects': objects
    }

    return render(request, 'web/list_view.html', context)


def detail_view(request, id):
    obj = Article.objects.get(id=id)
    context = {
        'object': obj
    }

    return render(request, 'web/detail_view.html', context)


def create_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'web/create_view.html', context)

def update_view(request,id=id):
    obj=Article.objects.get(id=id)
    form=ArticleForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'form':form,
        'obj':obj
    }
    return render(request,'web/create_view.html',context)
