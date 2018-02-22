from django.urls import path

from logs.views import (TopicList, TopicDetail,
                        TopicCreate, TopicUpdate, TopicDelete,
                        TopicAddEntry)


urlpatterns = [
        path('', TopicList.as_view(), name='logs_topic_list'),
        path('create/', TopicCreate.as_view(), name='logs_topic_create'),
        path('<slug:slug>/', TopicDetail.as_view(), name='logs_topic_detail'),
        path('<slug:slug>/update/', TopicUpdate.as_view(), name='logs_topic_update'),
        path('<slug:slug>/delete/', TopicDelete.as_view(), name='logs_topic_delete'),
        path('<slug:slug>/add_entry/', TopicAddEntry.as_view(), name='logs_topic_add_entry'),
        ]
