from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django_redis import get_redis_connection
from . import constants

from verifications.libs.captcha.captcha import captcha

# Create your views here.

class ImageCodeView(View):
    # 图形验证码
    def get(self, request, uuid):
        # uuid 通用唯一识别码,用于唯一标识该图形验证码属于哪个用户
        # return .image/jpg
        
        # 接受校验参数(已在uuid)

        # 生成图形验证码(使用captcha扩展)
        text, imgae = captcha.generate_captcha()

        # 保存图形验证码至redis数据库
        # 创建连接reids数据库的对象
        redis_conn = get_redis_connection('verify_code')
        # redis_conn.setex('key', 'expires', 'value')
        redis_conn.setex('img_%s'%uuid, constants.IMAGE_CODE_REDIS_EXPIRES, text)

        # 响应图形验证码
        return HttpResponse(imgae, content_type='image/jpg')
