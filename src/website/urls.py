from django.urls import path
from website.views import *


urlpatterns = [
    path('', home, name='home' ),
    #path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('record/<int:pk>', customer_record, name='record'),
    path('delete/<int:pk>', delete_record, name='delete'),
    path('add/', add_record, name='add'),
    path('update/<int:pk>', update_record, name='update'),
]