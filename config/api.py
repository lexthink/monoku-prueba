from apps.events.api.views import EventViewSet, StandViewSet
from apps.products.api.views import ProductViewSet, OptionViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', EventViewSet)
router.register('stands', StandViewSet)
router.register('products', ProductViewSet)
router.register('options', OptionViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
