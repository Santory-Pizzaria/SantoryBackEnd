from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import EnderecoViewSet, ItemPedidoViewSet, PedidoViewSet, ProdutoViewSet, UserViewSet, UsuarioViewSet
from core.views import BebidaViewSet, CarrinhoViewSet, CarrinhoItemViewSet, ComboViewSet, ReservaViewSet, PizzaViewSet
from core.views import FeedbackViewSet
router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'endereco', EnderecoViewSet, basename='endereco')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itempedido', ItemPedidoViewSet, basename='itempedido')
router.register(r'reservas', ReservaViewSet, basename='reserva')
router.register(r'pizzas', PizzaViewSet, basename='pizza')
router.register(r'combos', ComboViewSet, basename='combo')
router.register(r'carrinhos', CarrinhoViewSet, basename='carrinho')
router.register(r'carrinhoitens', CarrinhoItemViewSet, basename='carrinhoitem')
router.register(r'bebidas', BebidaViewSet, basename='bebida')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path('api/feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    # API
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
