from django.urls import path
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
    path('info_order/', info_order, name='info_order'),
]
