from django.conf.urls import url
from . import views

urlpatterns = [
    # 调试
    url(r'^sample/$', views.sample),
    # 分组获取正则数据,位置参数
    # http:127.0.0.1/categoryid/bookid/
    # url(r'^(\d+)/(\d+)/$',detail),
    # 分组获取正则数据,关键字参数
    # http:127.0.0.1/categoryid=?
    # as_view()返回的是一个视图函数名
    # 判断用户名是否有重复
    url(r'^usernames/(?P<username>[a-zA-Z_-]{5,20})/count/$', views.UsernameCountView.as_view()),
    # 用户注册 reverse(users:register) == '/register/'
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 判断手机号是否有重复
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
]
