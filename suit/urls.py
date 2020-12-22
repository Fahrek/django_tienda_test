from django.urls import path
from .views import home, contact, gallery, addProduct, listProduct, editProduct, deleteProduct, register

urlpatterns = [
    path('',                         home,          name='home'         ),
    path('contact/',                 contact,       name='contact'      ),
    path('gallery/',                 gallery,       name='gallery'      ),
    path('register/',                register,      name='register'     ),
    path('add-product/',             addProduct,    name='addproduct'   ),
    path('list-product/',            listProduct,   name='listproduct'  ),
    path('edit-product/<int:id>/',   editProduct,   name='editproduct'  ),
    path('delete-product/<int:id>/', deleteProduct, name='deleteproduct'),
]
