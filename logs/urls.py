from django.urls import path

from .views import (TopicList, TopicDetail,
                    TypeList, TypeDetail,)


app_name = 'logs'

urlpatterns = [
        path('topic/', TopicList.as_view(), name='topic_list'),
        path('topic/<slug:topic_slug>/', TopicDetail.as_view(), name='topic_detail'),
        path('type/', TypeList.as_view(), name='type_list'),
        path('type/<slug:type_slug>/', TypeDetail.as_view(), name='type_detail')
        ]
