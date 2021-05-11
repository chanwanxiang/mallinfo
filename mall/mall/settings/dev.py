# 开发环境配置文件

# Django settings for mall project.

# Generated by 'django-admin startproject' using Django 1.11.17.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.11/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.11/ref/settings/

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 查看项目导包路径
print(sys.path)
# 追加导包路径指向apps包
# sys.path.insert(0,'D:/isMe/mallinfo/mall/mall/apps')
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c=%x=4g7clph988a+r%g)#pl((-b)wqd(7648!vh#(iz)xw%22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# 注册应用需要模板迁移,验证功能无需依赖
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册用户子应用
    # 'mall.apps.users',
    # 追加到包路径后注册子应用
    'users',
    # 首页广告模块
    'contents',
    # 验证模块,注册一般需要模板或者迁移操作,验证可以注册也可以不注册
    'verifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mall.urls'

TEMPLATES = [
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.request',
    #             'django.contrib.auth.context_processors.auth',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     },
    # },
    {
        # 配置jinja2模板引擎
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # 配置模板文件加载路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 补充jiaja2模板引擎环境
            'environment': 'mall.utils.jinja2_env.jinja2_environment',
        },
    },
]

WSGI_APPLICATION = 'mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# django默认sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# 配置mysql
DATABASES = {
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 数据库主机
        'HOST': '47.98.188.248',
        # 数据库端口
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'meiduo'
    },
}

# 配置redis
CACHES = {
    # 默认
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.98.188.248:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # session
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.98.188.248:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 验证码
    "verify_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.98.188.248:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# session额外配置
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 指定加载静态文件路由前缀
STATIC_URL = '/static/'

# 配置静态文件加载路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 配置工程日志
LOGGING = {
    'version': 1,
    # 是否禁用已经存在的日志器
    'disable_existing_loggers': False,
    # 日志信息显示的格式
    'formatters': {
        'verbose': {
            # 等级 时间 模块 行数 信息
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            # 等级 模块 行数 信息
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    # 对日志进行过滤
    'filters': {
        # django在debug模式下才输出日志
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 日志处理方法
    'handlers': {
        # 向终端中输出日志
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 向文件中输出日志
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志文件的位置
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'logs/meiduo.log'),
            # 单个日志最大容量 300M
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    # 日志器
    'loggers': {
        # 定义了一个名为django的日志器
        'django': {
            # 可以同时向终端与文件中输出日志
            'handlers': ['console', 'file'],
            # 是否继续传递日志信息
            'propagate': True,
            # 日志器接收的最低日志级别
            'level': 'INFO',
        },
    }
}

# 指定自定义的用户模型类 语法 '子应用.用户模型类'
AUTH_USER_MODEL = 'users.User'
