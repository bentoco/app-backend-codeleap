from django.http import HttpResponse


def post(request):
    return request


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
