from django.shortcuts import render
from careforallapp.models import Post, Post1, Post2

# Create your views here.

def base(request):
    return render(request,'careforallapp/base.html')

def datasecurity(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'careforallapp/datasecurity.html',context=context)

def fitness(request):
    everypost=Post1.objects.all()
    context={"everypost":everypost}
    return render(request, "careforallapp/fitness.html", context)

def personality(request):
    ppost=Post2.objects.all()
    context={"ppost":ppost}
    return render(request, "careforallapp/personality.html", context)
