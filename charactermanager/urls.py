from django.urls import path

from . import views

app_name = 'charactermanager'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/playerlist/
    path('playerlist/', views.playerlist, name='playerlist'),
    # ex: /polls/characterlist/
    path('characterlist/', views.characterlist, name='characterlist'),
    # ex: /polls/5/
    path('playerdetail/<int:player_id>/', views.playerdetail, name='playerdetail'),
    # ex: /polls/5/
    path('characterdetail/<int:character_id>/', views.characterdetail, name='characterdetail'),
]
