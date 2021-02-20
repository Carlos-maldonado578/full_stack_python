from django.shortcuts import render, HttpResponse, redirect #controlar traspaso de datos.

def index(request):
    return HttpResponse('Marcador de posicion para mostrar más tarde una lista de todos los blogs')

def root(request):
    return redirect('blogs/')

def new(request):
    return HttpResponse('crear formulario de blog')

def create(request):
    return redirect('/')

def show(request, _numero, _nn):
    #print(type(_numero))
    try:
        int(_nn)
        return HttpResponse(f'Editar el blog {_numero}/{_nn}')
    except:
        #return HttpResponse('oasoajsoaj')
        return redirect(f'/blogs/{_numero}/edit/')


def edit(request, _numero):
    return HttpResponse(f'numero del blog {_numero}')

# Create your views here.
