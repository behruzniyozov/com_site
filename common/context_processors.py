from django.db import models

from accounts.models import User, CartItem

def common_context(request):
    cart_items = CartItem.objects.filter(cart=request.user.cart).annotate(
        total_price=models.F('quantity') * models.F('product_variant__price')
    ) if request.user.is_authenticated else []

    total_amount = sum(item.total_price for item in cart_items)

    return {'site_name': 'My E-commerce Site',
            'is_authenticated': request.user.is_authenticated,
            'user_cart_items_count': cart_items.count() if request.user.is_authenticated else 0,
            'cart_total_amount': total_amount // 100, }