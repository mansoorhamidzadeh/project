from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view

from .models import *
from .forms import *
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .serializers import ArticleSerializers


# Create your views here.

# generic Views
class MyView(ListView):
    model = Article
    template_name = 'web/list_view.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = Article.objects.filter(is_special=True)
        return queryset


class MyDetailView(DetailView):
    model = Article
    template_name = 'web/detail_view.html'
    context_object_name = 'object'

    # def get_object(self, queryset=None):
    #     pk=self.kwargs.get('pkk')
    #     return Article.objects.get(pk=pk)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['category'] = article.category.all()
        return context


class MyCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'web/create_view.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save
        return super(MyCreateView, self).form_valid(form)


class MyUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'web/create_view.html'
    success_url = '/'


class MyDeleteView(DeleteView):
    model = Article
    template_name = 'web/delete_view.html'
    success_url = '/'
# def list_view(request):
#     objects = Article.objects.all()
#
#     context = {
#         'objects': objects
#     }
#
#     return render(request, 'web/list_view.html', context)
#
#
# def detail_view(request, id):
#     obj = Article.objects.get(id=id)
#     category = ArticleCategory.objects.filter(article__title=obj.title)

#     context = {
#         'object': obj,
#         'category': category
#     }
#
#     return render(request, 'web/detail_view.html', context)
#
#
# def create_view(request):
#     form = ArticleForm()
#
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             print(request.user)
#             obj = form.save(commit=False)
#             obj.author = request.user
#             obj.save()
#             return redirect('/')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'web/create_view.html', context)
#
#
# def update_view(request, id=id):
#     obj = Article.objects.get(id=id)
#     form = ArticleForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {
#         'form': form,
#         'obj': obj
#     }
#     return render(request, 'web/create_view.html', context)
#
#
# def delete_view(request, id):
#     object = Article.objects.get(id=id)
#     context = {}
#     if request.method == 'POST':
#         object.delete()
#         return redirect('/')
#     return render(request, 'web/delete_view.html', context)




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
