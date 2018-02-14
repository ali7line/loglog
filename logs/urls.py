from django.urls import path

from .views import TopicList

app_name = 'logs'

urlpatterns = [
        path('topic/', TopicList.as_view(), name='topic_list'),
        ]
