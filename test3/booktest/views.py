from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse('aaa')

def detail(request, p1, p2, p3):
    return HttpResponse('%s-%s-%s'%(p1, p2, p3))
# get请求
def getTest1(request):
    return render(request, 'booktest/getTest1.html' )

def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/getTest2.html', context)

def getTest3(request):
    a1 = request.GET.getlist('a')
    context = {'a': a1}
    return render(request, 'booktest/getTest3.html', context)

# post请求
def postTest1(request):
    return render(request, 'booktest/postTest1.html', )

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    local = request.POST.getlist('local')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'local':local}
    return render(request, 'booktest/postTest2.html', context)
# 设置cookie值
def cookieTest(request):
    response=HttpResponse()
    response.set_cookie('t1','cookie')
    # cookie=request.COOKIES
    # if cookie.has_key('t1'):
    #     response.write(cookie['t1'])
    return response

# 重定向
def redTest1(request):
    return HttpResponseRedirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('重定向页面！')

# session
def session1(request):
    uname = request.session.get('myname','nologin')
    context = {'uname':uname}
    return render(request, 'booktest/session1.html', context)
def session2(request):
    return render(request, 'booktest/session2.html')
def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname']=uname
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')