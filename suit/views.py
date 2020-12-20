from django.shortcuts import render, redirect, get_object_or_404
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


def editProduct(request, id):
    # Product.object.get(id=id)

    product = get_object_or_404(Product, id=id)

    data = {
        'form': ProductForm(instance=product)
    }

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(to='listproduct')
        data['form'] = form

    return render(request, 'suit/producto/modificar.html', data)


def deleteProduct(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    return redirect(to='listproduct')
