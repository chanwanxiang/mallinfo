from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^image_code/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),
]
