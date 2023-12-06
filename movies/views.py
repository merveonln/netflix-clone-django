from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    filmler=Movie.objects.all()
    user=request.user.kullanici
    search=""
    if request.GET.get('search'):
        search=request.GET.get('search')
        filmler=Movie.objects.filter(
            Q(isim__icontains=search) |
            Q(kategori__isim__icontains=search)
        )
    context={
        'filmler': filmler,
        'user':user
    }
    return render(request, 'browse-index.html', context)
