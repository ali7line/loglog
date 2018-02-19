from django.urls import path

from logs.views import TypeList, TypeDetail, TypeCreate


urlpatterns = [
        path('', TypeList.as_view(), name='logs_type_list'),
        path('create/', TypeCreate.as_view(), name='logs_type_create'),
        path('<slug:type_slug>/', TypeDetail.as_view(), name='logs_type_detail')
        ]
