from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from apps.catalogo.views.admin.Product import ProductListView
from apps.catalogo.views.admin.Product import ProductCreateView
from apps.catalogo.views.admin.Product import ProductDeleteView
from apps.catalogo.views.admin.Product import ProductUpdateView

urlpatterns = patterns('',
                       url(r'^product/$',
                           ProductListView.as_view(),
                           name='product_list'),

                       url(r'^create/$',
                           ProductCreateView.as_view(),
                           name='product_create'),

                       url(r'^edit/(?P<pk>\d+)/$',
                           ProductUpdateView.as_view(),
                           name='product_edit'),

                       url(r'^delete/(?P<pk>\d+)/$',
                           ProductUpdateView.as_view(),
                           name='product_delete'),

                       )