from django.http           import Http404
from django.contrib        import messages
from django.core.paginator import Paginator
from django.contrib.auth   import authenticate, login
from django.shortcuts      import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Product
from .forms  import ContactForm, ProductForm, RegisterForm


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
            # data['msg'] = 'formulario enviado'
            messages.success(request, 'formulario enviado')
        else:
            data['form'] = form

    return render(request, 'suit/contacto.html', data)


#@login_required
def gallery(request):
    return render(request, 'suit/galeria.html')


@permission_required('suit.add_product')
def addProduct(request):
    data = {
        'form': ProductForm()
    }

    if request.method == 'POST':  # Validación pq el form devuelve los datos para guardarlos en la BD
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'producto guardado correctamente')
            # data['msg'] = 'producto guardado correctamente'
        else:
            data['form'] = form

    return render(request, 'suit/producto/agregar.html', data)


@permission_required('suit.view_product')
def listProduct(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)  # Recoge el número de la var 'page' desde la URL, si no existe devuelve 1

    try:
        paginator = Paginator(products, 5)  # Instancia del paginador al que se le pasa lista de prod. y num. de pág.
        products = paginator.page(page)  # Solo devuelve los registros del num. de pag. que tb se devuelve
    except:
        raise Http404  # Para cuando no existen registros en una pág. determinada

    data = {
        'entity': products,
        'paginator': paginator
    }

    return render(request, 'suit/producto/listar.html', data)


@permission_required('suit.change_product')
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
            messages.success(request, 'editado correctamente')
            return redirect(to='listproduct')
        data['form'] = form

    return render(request, 'suit/producto/modificar.html', data)


@permission_required('suit.delete_product')
def deleteProduct(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'eliminado satisfactoriamente')
    return redirect(to='listproduct')


def register(request):
    data = {
        'form': RegisterForm()
    }

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'registrado correctamente')
            return redirect(to='home')
        data['form'] = form

    return render(request, 'registration/registro.html', data)
