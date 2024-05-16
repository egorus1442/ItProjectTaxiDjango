from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', login_and_register, name='login_and_register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('history_trips/', history_trips, name='history_trips'),
    path('profile/', profile, name='profile'),
    path('infoorder/', info_order, name='info_order'),

]