from django.shortcuts import render
def index(request):
    name = "World"
    return render(request, 'base.html', {'name': name})

def book_search(request):
    search = request.GET.getlist('search') or ['No search term']
    return render(request, 'search-results.html', {'search': ' '.join(search)})