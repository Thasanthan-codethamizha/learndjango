from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
now = datetime.datetime.now()
monthdef = 12 - now.month


def index(request):
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1,
        "month": monthdef
    })
