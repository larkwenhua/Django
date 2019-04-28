# from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from django.shortcuts import render
from .models import *
def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    booklist = Bookinfo.objects.all()
    context = {'list':booklist}
    return render(request,'booktest/index.html', context)

def show(request, id):
    book = Bookinfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list1':herolist}
    return render(request, 'booktest/show.html', context)
