from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e_commerce_shop.products_app.urls', namespace='products_app')),
    path('basket/', include('e_commerce_shop.basket_app.urls', namespace='basket_app')),
    path('auth/', include('e_commerce_shop.app_auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
