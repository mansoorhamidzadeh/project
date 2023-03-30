from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework.decorators import api_view

from .models import *
from .forms import *
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .serializers import ArticleSerializers


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


def update_view(request, id=id):
    obj = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
        'obj': obj
    }
    return render(request, 'web/create_view.html', context)


class MyView(ListView):
    model = Article
    template_name = 'web/list_view.html'
    context_object_name = 'objects'


class MyDetailView(DetailView):

    template_name = 'web/detail_view.html'
    context_object_name = 'object '

    def get_object(self, queryset=None):
        return get_object_or_404(
            Article.objects.filter(pk=self.kwargs.get('pk'))
        )


class MyCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'web/create_view.html'
    success_url = '/'


class MyUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'web/create_view.html'
    success_url = '/'


# class ProductListCreateApiView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class PeoductCreateView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if content is None:
#             content = title
#         serializer.save(content=content)


# @api_view(['GET'])
# def Api(request, ):
#     if request.method == 'GET':
#         obj = Article.objects.all()
#         serializer = ArticleSerializers(obj, many=True)
#         return JsonResponse(serializer.data, safe=False)
