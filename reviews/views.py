from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
def index(request):
    name = "World"
    return render(request, 'base.html', {'name': name})

def book_search(request):
    search = request.GET.getlist('search') or ['No search term']
    return render(request, 'search-results.html', {'search': ' '.join(search)})

def welcome_view(request):
    message = (f"<html><h1>Welcome to Bookr!</h1>"
               f"<p>{Book.objects.count()} books and counting!</p>"
               f"</html>")
    return HttpResponse(message)
