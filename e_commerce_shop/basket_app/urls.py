from django.urls import path

from e_commerce_shop.basket_app.views import basket_summary

app_name = 'basket_app'

urlpatterns = (
    path('', basket_summary, name='basket_summary'),
)
