from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product


def home(request):
    # we are not using context
    context = {
        'goods': ['Home page'],
    }
    return render(request, 'products/home.html', context)


def productshome(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/productshome.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/productshome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_name', 'description']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_name', 'description']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.username:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/products/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.username:
            return True
        return False


def serviceshome(request):
    context = {
        'goods': ['Services page'],
    }
    return render(request, 'products/serviceshome.html', context)
