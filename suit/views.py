from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()  # Hace consulta y devuelve una lista de instancias de productos
    data = {
        'products': products
    }  # Creamos un diccionario a partir de la de lista de productos

    return render(request, 'suit/home.html', data)


def contact(request):
    return render(request, 'suit/contacto.html')


def gallery(request):
    return render(request, 'suit/galeria.html')
