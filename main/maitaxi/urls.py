from django.urls import path
from .views import *

urlpatterns = [
    path(route='', view=login_and_register, name='login_and_register'),
    path(route='login/', view=LoginUser.as_view(), name='login'),
    path(route='register/', view=RegisterUser.as_view(), name='register'),
    path(route='logout/', view=logout_user, name='logout'),
    path(route='home/', view=home, name='home'),
    path(route='about/', view=about, name='about'),
    path(route='history_trips/', view=history_trips, name='history_trips'),
    path(route='profile/', view=profile, name='profile'),
    path(route='info_order/', view=info_order, name='info_order'),
    path(route='edit-profile/', view=edit_profile, name='edit_profile'),
]
