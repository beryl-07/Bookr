from django.http import HttpResponse

def index(request):
    name = request.GET.get('name', 'world') or 'world'
    return HttpResponse(f'Hello {name}!')