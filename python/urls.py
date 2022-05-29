from django.contrib import admin
from django.urls import path

from familiares.views import familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', familiares, name = 'index'),
]
