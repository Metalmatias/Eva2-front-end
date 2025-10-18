from django.shortcuts import render,get_object_or_404
from .models import Categoria,Producto
# Create your views here.



def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos, 'categorias': categorias})

def productos_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'tienda/productos_por_categoria.html', {
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias
    })


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    return render(request, 'tienda/detalle_producto.html', {'producto': producto, 'categorias': categorias})
