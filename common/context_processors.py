from django.db import models
from accounts.models import User, CartItem
from django.core.exceptions import ObjectDoesNotExist

def common_context(request):
    site_context = {
        'site_name': 'Com_Site',
        'is_user_authenticated': request.user.is_authenticated,
        'user_cart_items_count': 0,
        'cart_total_amount': 0,
    }

    if request.user.is_authenticated:
        try:
            cart = request.user.cart
            cart_items = CartItem.objects.filter(cart=cart).annotate(
                total_amount=models.F('quantity') * models.F('product__price')
            )
            total_amount = sum(item.total_amount for item in cart_items)
            site_context['user_cart_items_count'] = cart.cart_items.count()
            site_context['cart_total_amount'] = total_amount // 100
        except ObjectDoesNotExist:
            pass  # Leave defaults (0)

    return site_context
