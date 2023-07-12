from django.urls import path
from .views import TeamView, TeamInfosView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamInfosView.as_view()),
]
