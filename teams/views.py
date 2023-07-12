from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from datetime import datetime as dt


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        team_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            team_list.append(team_dict)

        return Response(team_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        print(request.data)
        if request.data["titles"] < 0:
            return Response({"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST)

        current_year = dt.now().year
        first_cup_date = dt.strptime(request.data["first_cup"], "%Y-%m-%d").date()
        first_cup_year = first_cup_date.year

        if first_cup_year < 1930 or first_cup_year > current_year or (first_cup_year - 1930) % 4 != 0:
            return Response({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)

        if request.data["titles"] > (current_year - first_cup_year) / 4:
            return Response(
                {"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST
            )

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)


class TeamInfosView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
