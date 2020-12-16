from django.urls import path
from .views import home, contact, gallery

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
]
