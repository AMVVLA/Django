from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def login(request):
    return HttpResponse('로그인 페이지')

def signout(request):
    return HttpResponse("잘가~")

def test(request):
    return HttpResponse("머지가 머지")