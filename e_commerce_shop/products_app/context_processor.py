from e_commerce_shop.products_app.models import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }

