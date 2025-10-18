from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='home'),
    path('categoria/<slug:categoria_slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]
