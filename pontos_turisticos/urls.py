
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from endereco.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
	path('api-token/', views.obtain_auth_token),
	path('',include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
