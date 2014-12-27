from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from apps.catalogo.views.Home import LoginView
from apps.catalogo.views.Home import SignUpView
from apps.catalogo.views.Home import LogoutView

urlpatterns = patterns('',
                       url(r'^$',
                           TemplateView.as_view(template_name='home.html'),
                           name='home'),

                       url(r'^login/$',
                           LoginView.as_view(),
                           name='login'),

                       url(r'^register/$',
                           SignUpView.as_view(),
                           name='sign_up'),
                       url(r'^logout/$',
                           LogoutView.as_view(),
                           name='logout'),

                       url(r'^admin/', include('apps.catalogo.urls.admin')),

                       )