from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
from django.db.models import Q


def home(request):
    # we are not using context
    context = {
        'goods': ['Home page'],
    }
    return render(request, 'products/home.html', context)


# def productshome(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'products/productshome.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/productshome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        print(f"Current username: {self.request.user}, type: {type(self.request.user)}")

        if not self.request.user.is_anonymous:
            result = Product.objects.filter(~Q(username=self.request.user) & Q(available=True)).order_by('-date_posted')
            print(f"result: {result}")
            return result

        return Product.objects.filter(Q(available=True)).order_by('-date_posted')


class UserProductListView(ListView):
    model = Product
    template_name = 'products/user_products.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        print(f"Current username: {self.kwargs.get('username')}")
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(username=user).order_by('-date_posted')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_name', 'description', 'category', 'image']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_name', 'description', 'image']

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
