from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.CreateMovieView.as_view(), name='create'),
    path('update/', views.UpdateMovieView.as_view(), name='update'),
]
