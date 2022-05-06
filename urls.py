from django.conf.urls import url

from . import views


urlpatterns = [

    # ---------BD_GEOINFO--------#
    url(r'^ajax/district_list/', views.ajax_district_list.as_view(),
        name='ajax_district_list'),

]
