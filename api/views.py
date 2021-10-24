from django.shortcuts import render
from django.http import Http404,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Team, Tournament, TournamentDetail, User
from .serializers import GameSerializer, TeamSerializer, TourneySerializer, TourneyDetailSerializer
from django.db.models import Q

# Create your views here.
class Tournaments(APIView):
    def get(self, request, format=None):
        turn = Tournament.objects.filter(status='regis_open')
        serializer = TourneySerializer(turn, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def recomend_tourney(request, user_id):
    team = Team.objects.filter(Q(created_by=user_id) & Q(status=True))
    det = TournamentDetail.objects.filter(teams=team)
    serialDet = TourneyDetailSerializer(det, many=True)
    tour = Tournament.objects.filter(Q(status='regis_open'))
    serialtour = TourneySerializer(tour, many=True)
    return Response(serialtour.data)