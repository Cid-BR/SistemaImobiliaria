#url contas
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from SistemaImobiliaria.contas import views

urlpatterns = [

#    url(r'^$', views.index),
    url(r'^$', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
