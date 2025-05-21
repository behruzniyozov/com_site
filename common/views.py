from django.views.generic import TemplateView

from products.models import Category, FeaturedProduct


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        featured_products = FeaturedProduct.objects.filter(is_featured=True)
        latest_products = featured_products.order_by('-created_at')[:6]

        context['title'] = 'VooCommerce | Home'
        context['categories'] = categories
        context['featured_products'] = featured_products
        context['latest_products'] = latest_products
        print(categories[1].image.url)
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Contact Us'
        return context
