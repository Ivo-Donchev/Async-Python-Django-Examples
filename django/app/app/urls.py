from django.contrib import admin
from django.urls import path

from .views import view_with_multiprocessing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('multiprocessing/', view_with_multiprocessing)
]
