import re

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden
# from users.models import User
from django.db import DatabaseError

# Create your views here.

# 函数视图
def sample(request):
    return HttpResponse('sample')

# 类视图
class RegisterView(View):
    # 用户注册
    def get(self,request):
        # 提供用户注册页面
        return render(request,'register.html')

    def post(self, request):
        # 实现用户注册业务逻辑

        # 接收参数 value = request.POST.get('key')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        # 校验参数
        # 判断参数是否齐全,如果此时参数还是出错,说明该请求是非正常渠道发送的,所以直接禁止本次请求
        # all([列表]):校验列表中的元素是否为空,只要有一个为空,返回FALSE
        if not all([username, password, password2, mobile, allow]):
            return HttpResponseForbidden('缺少必传参数')
        # 判断用户名是否5-20个字符
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return HttpResponseForbidden('请输入5-20个字符的用户名')
        # 判断密码是否8-20个数字
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return HttpResponseForbidden('请输入8-20位密码')
        # 判断两次密码是否一致
        if password != password2:
            return HttpResponseForbidden('两次输入的密码不一致')
        # 判断手机号是否合法
        if not re.match(r'1[3-9]\d{9}$', mobile):
            return HttpResponseForbidden('请输入正确的手机号码')
        # 判断用户是够勾选用户协议
        if allow != 'on':
            return HttpResponseForbidden('请勾选用户协议')

        # 保存注册数据(注册业务核心)
        try:
            User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError as errorms:
            print(errorms)
            return render(request, 'register.html', {'register_errormsg':'注册失败'})

        # 响应注册结果(重定向到首页)
        return HttpResponse('注册成功,重定向到首页')
