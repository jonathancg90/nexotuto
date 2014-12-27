# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView

from apps.common.access import LoginRequiredMixin
from apps.catalogo.forms.ProductForm import ProductForm
from apps.catalogo.models.Product import Product



class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'admin/product/list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product/create.html'

    def get_success_url(self):
        return reverse('product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product/update.html'

    def get_success_url(self):
        return reverse('product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'admin/product/delete.html'

    def get_success_url(self):
        return reverse('product_list')


