from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tournaments/', views.Tournaments.as_view(), name='tournaments'),
    path('recomended_tournaments/<int:user_id>', views.recomend_tourney),
]