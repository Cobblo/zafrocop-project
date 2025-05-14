"""
URL configuration for Zafrocop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from store import views

urlpatterns = [
    path('secureadmin/', admin.site.urls),  # Real admin login here
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),  # Fake admin
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),


    # orders
    path('orders/', include('orders.urls')),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('policy/', views.privacy_policy, name='privacy_policy'),
    path('return-and-refund/', views.return_and_refund, name='return_and_refund'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
