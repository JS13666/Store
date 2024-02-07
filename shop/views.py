from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.core.paginator import Paginator


def product_list(request, category_slug=None, page=1):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))
    slag_url = category_slug

    return render(request, 'shop/list.html', {'category': category, 'categories': categories, 'products': current_page, 'slug_url': slag_url})


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'product': product, 'cart_product_form': cart_product_form})
