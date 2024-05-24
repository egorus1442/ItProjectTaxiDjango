from django.contrib import admin
from django.urls import path, include
from maitaxi.views import e_handler404, e_handler500

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='', view=include(arg='maitaxi.urls')),
]

handler404 = 'maitaxi.views.e_handler404'
handler500 = 'maitaxi.views.e_handler500'
