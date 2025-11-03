from django.urls import path
from . import views

app_name = "prices"

urlpatterns = [
    path("", views.btc_view, name="home"),
    path("watch/", views.watch_list, name="watch_list"),
    path("watch/new/", views.watch_create, name="watch_create"),
    path("watch/edit/<int:pk>/", views.watch_update, name="watch_update"),
    path("watch/delete/<int:pk>/", views.watch_delete, name="watch_delete"),
]
