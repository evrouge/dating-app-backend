from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt 
# this is for the user login

urlpatterns = [
    path('api/dating', views.DatingList.as_view(), name='dating_list'),
    path('api/dating/<int:pk>', views.DatingDetail.as_view(), name='dating_detail'),
    path('api/dating/login', csrf_exempt(views.check_login), name="check_login") # api/useraccount/login will be routed to the check_login function for auth
]