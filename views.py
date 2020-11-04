from django.shortcuts import render
from .models import Book

# Create your views here.


def bstore(request):
    count = Book.objects.all().count()
    context = {'count': count,
    }
    request.session['location'] = "unknown"  # Session variable
    if request.user.is_authenticated:        # Is the user authenticated?
            request.session['location'] = "Earth"
    return render(request, 'bstore.html', context)

    #return render(request, 'bstore.html', context)

def template(request):
    return render(request, 'template.html')

