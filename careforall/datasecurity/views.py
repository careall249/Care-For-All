from django.shortcuts import render
from datasecurity.models import Post

# Create your views here.
def datasecurity(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'datasecurity/data.html',context=context)

def blogHome(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "datasecurity/blogHome.html", context)
