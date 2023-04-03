from django.urls import path
from .views import *
app_name='api'
urlpatterns=[
    path('',ArticleList.as_view(),name='list'),
    path('<int:pk>/',ArticleDetail.as_view(),name='detail'),
    path('users/',Users.as_view()),
    path('users/<int:pk>/',UserDetail.as_view()),

]