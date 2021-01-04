from django.shortcuts import render
from personality.models import Post
# Create your views here.
def personality(request):
    ppost=Post.objects.all()
    context={"ppost":ppost}
    return render(request, "personality/personal.html", context)

def blogpersonal(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "personality/blogpersonal.html", context)
