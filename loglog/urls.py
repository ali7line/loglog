from django.contrib import admin
from django.urls import path, include

import logs.urls as logs_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(logs_url, namespace='logs'))
]
