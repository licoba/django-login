from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

def login(request):
    return render(request,'booktest/login.html')

def login_check(request):
    '''登录校验'''
    '''1、获取提交的用户名和密码'''
    # print(request.POST)#QueryDict 类型的对象，和字典的区别是：一个键可以对应多个值（通过getlist方法来获取多个值）
    password = request.POST.get('password')
    username = request.POST.get('username')


    '''2、校验'''

    if username == '小火鸡' and password == '123':
        #跳转到首页
        return redirect('/index')
    else:
        # 跳转到登录页面
        return redirect('/login')
    '''3、返回应答'''

def test_ajax(request):
    return render(request,'booktest/test_ajax.html')

def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == "123" and password == "123":
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def ajax_handle(request):
    return JsonResponse({'res':1})