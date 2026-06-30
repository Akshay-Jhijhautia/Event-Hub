from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ReservationViewSet

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='event')
router.register(r'reservation', ReservationViewSet, basename='reservation')

urlpatterns = router.urls