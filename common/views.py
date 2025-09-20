from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HTTPResponse:
    return render(request, "index.html")
