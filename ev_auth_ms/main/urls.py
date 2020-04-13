from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from app.evauth import views as account_views

# Setup the ViewSet Router
router = DefaultRouter()
router.register(r'users', account_views.UserViewSet)

urlpatterns = [
    # Core Routed URLs
    url(r'^reg/', include(router.urls)),

    # Auth URLs
    url(r'^reg/auth/', include('app.evauth.urls')),

    # Browsable API
    url(r'^reg-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
