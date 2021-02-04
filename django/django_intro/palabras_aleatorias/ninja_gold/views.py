from django.shortcuts import render, HttpResponse, redirect
from random import choice
import random
import datetime
now = datetime.datetime.now()
now_hora = now.strftime('(%d/%m/%Y %H:%M:%S)')

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 0
        request.session['my_list'] = []
    return render(request, "ninja_index.html")

def farm(request):
    num = random.randint(10,20)
    request.session['counter'] += num
    request.session['my_list'].append(f"Earned {num} golds from the Farm! {now_hora}")
    return render(request, "ninja_index.html")

def cave(request):
    num = random.randint(5,10)
    request.session['counter'] += num
    request.session['my_list'].append(f"Earned {num} golds from the Cave! {now_hora}")
    return redirect('/ninja_gold/')

def house(request):
    num = random.randint(2,5)
    request.session['counter'] += num
    request.session['my_list'].append(f"Earned {num} golds from the house! {now_hora}")
    return redirect('/ninja_gold/')

def casino(request):
    num = random.randint(0,50)
    opcion = ['earns', 'takes']
    num_opcion = choice(opcion)

    if num_opcion == 'earns':
        request.session['my_list'].append(f"Earned {num} golds from the Casino! {now_hora}")
        request.session['counter'] += num
    else:
        if request.session['counter'] < num:
            request.session['counter'] = 0
        else:
            request.session['counter'] -= num
            request.session['my_list'].append(f"Entered a casino {num} golds..Ouch. {now_hora}")
    return redirect('/ninja_gold/')


#request.session['my_list'].append("new item")
# Create your views here.
