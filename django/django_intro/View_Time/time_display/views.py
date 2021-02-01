from django.shortcuts import render
from time import gmtime, localtime, strftime


def index(request):
    ahora = localtime()
    context = {
        "date": strftime("%b %d, %Y", ahora),
        "time": strftime("%I:%M %p", ahora)
    }
    return render(request, 'index.html', context)

# Create your views here.
