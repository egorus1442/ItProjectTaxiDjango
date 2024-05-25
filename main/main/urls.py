from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='', view=include(arg='maitaxi.urls')),
]

handler404 = 'maitaxi.views.e_handler404'
handler500 = 'maitaxi.views.e_handler500'
