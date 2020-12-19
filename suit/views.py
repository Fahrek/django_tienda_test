from django.shortcuts import render
from .models import Product
from .forms import ContactForm, ProductForm


def home(request):

    products = Product.objects.all()  # Hace consulta y devuelve una lista de instancias de productos

    data = {
        'products': products
    }  # Creamos un diccionario a partir de la de lista de productos

    return render(request, 'suit/home.html', data)


def contact(request):

    data = {
        'form': ContactForm()
    }

    if request.method == 'POST':
        form = ContactForm(data=request.POST)  # El POST es un diccionario que tiene todos los datos del form
        if form.is_valid():
            form.save()
            data['msg'] = 'formulario enviado'
        else:
            data['form'] = form

    return render(request, 'suit/contacto.html', data)


def gallery(request):

    return render(request, 'suit/galeria.html')


def addProduct(request):

    data = {
        'form': ProductForm()
    }

    if request.method == 'POST':  # Validación pq el form devuelve los datos para guardarlos en la BD
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            data['msg'] = 'producto guardado correctamente'
        else:
            data['form'] = form

    return render(request, 'suit/producto/agregar.html', data)


def listProduct(request):

    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'suit/producto/listar.html', data)
