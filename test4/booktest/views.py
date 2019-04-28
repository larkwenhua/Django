from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    # hero=HeroInfo.objects.get(pk=3)
    # context={'hero':hero}
    list=HeroInfo.objects.filter(isDelete=False)
    context = {'list':list}
    return render(request, 'booktest/index.html', context)

def show(request, id):
    context={'id':id}

    return render(request, 'booktest/show.html', context)