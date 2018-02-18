from django.urls import path

from logs.views import TopicList, TopicDetail, TopicCreate


urlpatterns = [
        path('', TopicList.as_view(), name='logs_topic_list'),
        path('create/', TopicCreate.as_view(), name='logs_topic_create'),
        path('<slug:topic_slug>/', TopicDetail.as_view(), name='logs_topic_detail'),
        ]
