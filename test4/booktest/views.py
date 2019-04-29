from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
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

# 模版的继承
def index2(request):
    return render(request,'booktest/index2.html')
def user1(request):
    context = { 'uname':"dog"}
    return render(request, 'booktest/user1.html', context)
def user2(request):
    return render(request, 'booktest/user2.html')

# html专义
def htmlTest(request):
    context = {'t1':"<h1>123</h1>"}
    return render(request, 'booktest/htmlTest.html', context)

# csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

#验证码
def verifyCode(request):

    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("static/KumoFont.ttf", 38)
    # font_obj = ImageFont.load_default().font
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(4):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20 + 40 * i, 0), tmp, fill=get_random_color(), font=font_obj)

    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    width = 220  # 图片宽度（防止越界）
    height = 35
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=get_random_color())

    # 加干扰点
    for i in range(40):
        draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()

    return HttpResponse(data)

def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')

def verifyTest2(request):

    code1=request.POST['code_new']
    code2=request.session['valid_code']

    if code1==code2:
        return HttpResponse("ok")
    else:
        return HttpResponse("no")