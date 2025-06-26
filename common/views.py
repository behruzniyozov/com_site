from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db import models
from .forms import CheckoutForm

from products.models import Category, FeaturedProduct, Product, ProductReview, Comment, ProductVariant
from accounts.models import CartItem

from .forms import ContactMessageForm
from .models import ContactMessage


def contact_message_handler(request):
    form = ContactMessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Safe: Only access cleaned_data after validation
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return render(request, 'index.html')  # Or use redirect

    # Either GET request or invalid form
    return render(request, 'contact.html', {'form': form})

    return HttpResponse('Invalid request method.')



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        featured_products = FeaturedProduct.objects.filter(is_featured=True)
        latest_products = featured_products.order_by('-created_at')[:6]
        review_products = ProductReview.objects.select_related('product').order_by('-created_at')[:6]
        comments= Comment.objects.select_related('product').order_by('-created_at')[:6]


        context['title'] = 'ComSite | Home'
        context['categories'] = categories
        context['featured_products'] = featured_products
        context['latest_products'] = latest_products
        context['review_products'] = review_products 
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Contact Us'
        return context

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class BlogDetailView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Blog Detail'
        return super().get_context_data(**kwargs)


class ShopGridView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'

    def get_context_data(self, **kwargs):
        cart_items = CartItem.objects.filter(cart=self.request.user.cart).annotate(
            total_amount=models.F('quantity') * models.F('product__price')
        )
        

        context = super().get_context_data(**kwargs)
        context['cartitems'] = cart_items
        

        return context


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Profile'
        context['current_user'] = self.request.user
        return context
    
def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # You can process the data here or save it to the database
            print(form.cleaned_data)  # Just for debug/log
            return redirect('success')  # Replace with your actual success URL
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def product_detail_view(request, slug):
    product = Product.objects.get(slug=slug)
    variant = ProductVariant.objects.filter(product=product, is_active=True).first()

    return render(request, 'product_detail.html', {
        'product': product,
        'variant': variant
    })
