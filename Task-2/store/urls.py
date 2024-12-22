from django.urls import path

from store import views


urlpatterns = [
    path('', views.get_top_categories, name='home'),
]
