from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blog")

def blogs(request):
    return HttpResponse('marcador de posición para mostrar más tarde una lista de todos los blogs')

def new(request):
    return HttpResponse('marcador de posición para mostrar un nuevo formulario para crear un nuevo blogs')

def create(request):
    return redirect('/')

def show(request, _numero):
    return HttpResponse(f'marcador de posición para mostrar el numero de blog {_numero}')

def edit(request, _numero):
    return HttpResponse(f'Marcador de posición para editar el blog número {_numero}')

def delete(request, _numero):
    return redirect('/blog')


def json(request):
    content = {
        'num_blogs': 2,
        'blogs':['blog de la fena', 'Empleos publicos']
    }
    return JsonResponse(content)
# Create your views here.