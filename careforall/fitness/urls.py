from django.conf.urls import url

from . import views

app_name = 'fitness'

urlpatterns = [
    url(r'^$', views.fitness, name="fitness"),
    url(r'^fitness/(?P<slug>[^/]+)', views.blogfit, name='blogfit')
]
