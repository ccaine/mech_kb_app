from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "gb_home.html", {})


def groupbuy_view(request):
    return render(request, "gb_list.html", {})
