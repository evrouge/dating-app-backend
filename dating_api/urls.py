from django.urls import path
from . import views

urlpatterns = [
    path('api/dating', views.DatingList.as_view(), name='dating_list'),
    path('api/dating/<int:pk>', views.DatingDetail.as_view(), name='dating_detail')
]
