from django.urls import path
from . import views

urlpatterns = [
    path('main_menu/', views.MainMenuView.as_view()),


]

