from django.shortcuts import render
from time import gmtime, strftime


def index(request):
    ahora = gmtime()
    context = {
        "date": strftime("%b %d, %Y", ahora),
        "time": strftime("%I:%M %p", ahora)
    }
    return render(request, 'index.html', context)

# Create your views here.
