from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render


def index_view(request: HttpRequest) -> HTTPResponse:
    return render(request, "index.html")

def about_view(request: HttpRequest) -> HTTPResponse:
    return render(request, "common/about.html")
