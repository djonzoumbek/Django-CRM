from django.urls import path
from website.views import *


urlpatterns = [
    path('', home, name='home' ),
    #path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]