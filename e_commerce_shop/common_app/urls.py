from django.urls import path, include

from e_commerce_shop.common_app.views import AboutView, ContactView, ContactSuccessView

app_name = 'common_app'

urlpatterns = (
    path('', AboutView.as_view(), name='about-page'),
    path('contact/', ContactView.as_view(), name='contact-page'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact-success-page'),
)
