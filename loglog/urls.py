from django.contrib import admin
from django.urls import path, include

from logs.urls import (
        topic as topic_url,
        type as type_url,
        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topic/', include(topic_url)),
    path('type/', include(type_url)),
]
