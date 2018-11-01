# -*- coding: utf-8 -*-


from django.conf.urls import url
from lite.views import *



urlpatterns = [

    url(r'^user/login/$', Login.as_view()),
    url(r'^wx/create/$', WXCreate.as_view()),
    url(r'^wx/callback/$', WXCallback.as_view()),
    url(r'^image/get_list/$', ImageGetList.as_view()),

    url(r'^upload/get/token/$', UploadGetToken.as_view()),

    # url(r'^my/example/$', MyExample.as_view()),

]