from django.urls import path

from logs.views import TypeList, TypeDetail


urlpatterns = [
        path('', TypeList.as_view(), name='logs_type_list'),
        path('<slug:type_slug>/', TypeDetail.as_view(), name='logs_type_detail')
        ]
