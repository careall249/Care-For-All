from django.shortcuts import render
from fitness.models import Post
# Create your views here.
def fitness(request):
    everypost=Post.objects.all()
    context={"everypost":everypost}
    return render(request, "fitness/fit.html", context)


def blogfit(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "fitness/blogfit.html", context)
