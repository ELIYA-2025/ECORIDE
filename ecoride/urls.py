from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect # <-- Add this import

def api_redirect(request):
    return redirect('api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('eco_users.urls')),
    path('', api_redirect),  # <-- Add this line
]