"""shopy_science_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from item.views import ItemViewSet
from order.views import OrderViewSet, export
from contact.views import ConactViewSet
from ordered_item.views import OrderedItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename="items")
router.register(r'ordreditems', OrderedItemViewSet, basename="ordreditems")
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'contacts', ConactViewSet, basename="contacts")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('flow/orders_to_csv/', export),
    #Authentication Path 
    path('authentication/', include('dj_rest_auth.urls')),
    #Registration Path
    path('authentication/registration/', include('dj_rest_auth.registration.urls'))
]
