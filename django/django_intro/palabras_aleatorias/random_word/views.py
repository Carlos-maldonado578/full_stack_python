from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['counter'] = 0
    return render(request,"index.html")


def random_word(request):
    request.session['counter'] += 1
    context = {
        'unique_id': get_random_string(14)
    }
    return render(request,"index.html",context)

def reset(request):
    return redirect('/success')


def success(request):
    return render(request,"succes.html")


# Create your views here.
