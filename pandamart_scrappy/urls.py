from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('pandamart_scrappy', PandamartScrapperView, basename='pandamart-scrappy')
# router.register('logout', UserLogoutView, basename='user-logout')


urlpatterns = [
    path('', include(router.urls)),
]