from django.conf.urls import url

from . import views

app_name = 'personality'

urlpatterns = [
    url(r'^$', views.personality, name="personality"),
    url(r'^personality/(?P<slug>[^/]+)', views.blogpersonal, name='blogpersonal')
]
