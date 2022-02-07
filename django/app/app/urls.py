from django.contrib import admin
from django.urls import path

from .views import (
    async_view,
    view_with_threading,
    view_with_multiprocessing,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('multiprocessing/', view_with_multiprocessing),
    path('threading/', view_with_threading),
    path('async/', async_view),
]
