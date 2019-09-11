# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Welcome to the test to find your personal point on the "
    #     "Inglehart–Welzel Cultural Map!")

    return render(request, 'base.html')