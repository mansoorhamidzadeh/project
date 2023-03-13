from django.urls import path
from . import views
urlpatterns=[
    path('',views.list_view,name='list_view'),
    path('detail/<int:id>/',views.detail_view,name='detail_view'),
    path('create/',views.create_view,name='create'),
    path('update/<int:id>/',views.update_view,name='update'),
    path('api/',views.Api),
    path('ap/',views.ProductListCreateApiView.as_view()),
    path('ap/<int:pk>/',views.ProductDetailView.as_view()),
    path('ap/create/',views.PeoductCreateView.as_view())
]