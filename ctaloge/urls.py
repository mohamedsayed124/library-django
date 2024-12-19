from django.urls import path
from . import views
from . import models
urlpatterns=[
    path('', views.index ,name='index'),
    path('booklist', views.BookListView.as_view (),name='booklist'),
    path('book/<int:pk>', views.BookDetail.as_view (),name='bookdetail'),
    


]