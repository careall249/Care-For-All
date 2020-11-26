from django.conf.urls import url
from careforallapp import views

#URLs

app_name = 'careforallapp'

urlpatterns = [
    url(r'register/$', views.register, name='register')

]
