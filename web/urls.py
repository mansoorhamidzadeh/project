from django.urls import path
from . import views
urlpatterns=[
    path('',views.list_view,name='list_view'),
    path('detail/<int:id>/',views.detail_view,name='detail_view'),
    path('create/',views.create_view,name='create'),
    path('update/<int:id>/',views.update_view,name='update'),
    path('api/',views.Api),
    path('genview/',views.MyView.as_view()),
    path('genview/<int:pk>/',views.MyDetailView.as_view()),
    path('genview/create/',views.MyCreateView.as_view()),
    path('genview/update/<int:pk>/',views.MyUpdateView.as_view()),
    # path('ap/',views.ProductListCreateApiView.as_view()),
    # path('ap/<int:pk>/',views.ProductDetailView.as_view()),
    # path('ap/create/',views.PeoductCreateView.as_view())
]