from django.urls import path
from .views import register_customer, register_driver # <-- Changed import names
from django.shortcuts import redirect

def api_redirect(request):
    return redirect('register_customer')

urlpatterns = [
    path('register/customer/', register_customer, name='register_customer'), # <-- Removed .as_view()
    path('register/driver/', register_driver, name='register_driver'),       # <-- Removed .as_view()
    path('', api_redirect),
]