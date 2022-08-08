from rest_framework.routers import DefaultRouter

from mainapp.views import CategoryViewSet, ProductViewSet, RaitingViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')
router.register('raitings', RaitingViewSet, basename='raitings')

urlpatterns = []

urlpatterns += router.urls
