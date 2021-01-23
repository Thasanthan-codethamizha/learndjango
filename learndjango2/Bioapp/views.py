from django.shortcuts import render

from . import models
# Create your views here.


def index(request):
    key = models.Bio.objects.all()
    return render(request, "index.html")
