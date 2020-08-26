from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("shows", views.shows),
    path("shows/new", views.add_new_show),
    path("shows/create", views.create_show),
    path("shows/<int:showID>", views.show_info),
    path("shows/<int:showID>/destroy", views.delete_show),
    path("shows/<int:showID>/edit", views.edit_show),
    path("shows/<int:showID>/update", views.update_show)
]
