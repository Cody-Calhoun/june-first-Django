from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("Hello World")


def another(request, name):
    return HttpResponse(f"This is another one. Hello {name}")


def hello(request):
    return render(request, "index.html")


def redirected(request):
    return redirect('/unicorn')


def complete(request):
    return render(request, "redirect.html")


def catch_all(request, resource):
    return render(request, 'catch.html')
