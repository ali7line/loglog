from django.urls import path

from logs.views import (TypeList, TypeDetail,
                        TypeCreate, TypeUpdate, TypeDelete)


urlpatterns = [
        path('', TypeList.as_view(), name='logs_type_list'),
        path('create', TypeCreate.as_view(), name='logs_type_create'),
        path('<slug:slug>/', TypeDetail.as_view(), name='logs_type_detail'),
        path('<slug:slug>/update', TypeUpdate.as_view(), name='logs_type_update'),
        path('<slug:slug>/delete', TypeDelete.as_view(), name='logs_type_delete'),
        ]
