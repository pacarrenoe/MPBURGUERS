from django.urls import path
from .views import home, menu, nosotros, pedido

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('nosotros/', nosotros, name='nosotros'),
    path('pedido/', pedido, name='pedido'),

]