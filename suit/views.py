from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'suit/home.html')


def contact(request):
    return render(request, 'suit/contacto.html')


def gallery(request):
    return render(request, 'suit/galeria.html')
