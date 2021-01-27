from django.shortcuts import render,HttpResponse, redirect

def root(request):
    return redirect("/blog")

def index(request):
    return HttpResponse('marcador de posición para mostrar más tarde una lista de todos los blogs')

def new(request):
    return HttpResponse('marcador de posición para mostrar un nuevo formulario para crear un nuevo blogs')

def create(request):
    return redirect('/')

def show(request, _numero):
    return HttpResponse(f'marcador de posición para mostrar el numero de blog {_numero}')

def editar(request, _numero):
    return HttpResponse(f'Muestra la cadena: marcador de posición para mostrar el numero de blog {_numero}')

def delete(request, _numero):
    return redirect('/blog')


def json(request):
    return render(request, 'json.html')

# Create your views here.