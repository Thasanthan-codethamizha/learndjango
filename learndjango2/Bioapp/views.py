from django.shortcuts import render

from .models import Bio
# Create your views here.


def index(request):
    users = Bio.objects.all()
    return render(request, "index.html", {
        'users': users,
    })
