# basket_app.views.py
from django.shortcuts import render


def basket_summary(request):
    return render(request, 'basket/summary.html')
