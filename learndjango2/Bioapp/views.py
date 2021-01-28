from django.shortcuts import render

from .models import Bio
# Create your views here.


def index(request):
    users = Bio.objects.all()
    return render(request, "index.html", {
        'users': users,
    })


def add(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('email'):
            userform = Bio()
            userform.name = request.POST.get('name')
            userform.age = request.POST.get('age')
            userform.email = request.POST.get('email')
            userform.profile_pic = request.POST.get('image')
            userform.save()
    return render(request, "add.html")
