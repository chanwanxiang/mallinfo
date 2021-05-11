from django.http.response import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django_redis import get_redis_connection
from . import constants

from mall.utils.response_code import RETCODE


from verifications.libs.captcha.captcha import captcha

# Create your views here.

class SmsCodeView(View):
    # 短信验证码
    def get(self, request, mobile):
        # params    : mobile 手机号
        # return    : json

        # 接收参数
        image_code_cli = request.GET.get('image_code')
        uuid = request.GET.get('uuid')

        # 校验参数
        if not all([image_code_cli, uuid]):
            return HttpResponseForbidden('缺少必传参数')

        # 提取图形验证码
        redis_conn = get_redis_connection('verify_code')
        img_code_server = redis_conn.get('img_%s' %uuid)

        if img_code_server is None:
            return JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg':'图形验证码已失效'})

        # 删除图形验证码
        redis_conn.delete('img_%s' %uuid)
        # 对比图形验证码
        # 转小写,将bytes转字符串再对比
        img_code_server = img_code_server.decode()
        if image_code_cli.lower() != img_code_server.lower():
            return JsonResponse({'code':RETCODE.IMAGECODEERR, 'errmsg':'图形验证码有错误'})
        # 生成短信验证码
        # 发送短信验证码
        # 响应结果
        pass

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
