# url principal
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from SistemaImobiliaria import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^test/', views.test),
    url(r'^imobiliaria/', include('SistemaImobiliaria.Imobiliaria.urls',
    namespace='imobiliaria')),
    url(r'^contas/', include('SistemaImobiliaria.contas.urls',
    namespace='contas')),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
