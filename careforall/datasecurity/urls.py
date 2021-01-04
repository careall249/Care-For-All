from django.conf.urls import url

from . import views

app_name = 'datasecurity'

urlpatterns = [
    url(r'^$', views.datasecurity, name="datasecurity"),
    url(r'^datasecurity/(?P<slug>[^/]+)', views.blogHome, name='blogHome')
]
