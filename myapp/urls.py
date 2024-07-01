from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet , ReservationCreateView ,ReservationViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/reservations/', ReservationCreateView.as_view(), name='reservation-create')
    
]
