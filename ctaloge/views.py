from django.shortcuts import render
from . import models
from django.views import generic
# Create your views here.
def index(request):
    num_books= models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
    context={
        'num_books':num_books, 
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        
    }
    return render(request , 'index.html',context)




class BookListView(generic.CreateView):
    model = models.Book
    fields = '__all__'
    success_url = '/ctaloge'
    template_name = 'book_list.html'


class BookDetail(generic.DetailView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'books'

