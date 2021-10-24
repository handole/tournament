from rest_framework import serializers
from .models import User, Game, Team, Tournament, TournamentDetail
from drf_writable_nested import WritableNestedModelSerializer
from .utils import ResourceRelatedTeamField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'status']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'status']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class TourneyDetailSerializer(serializers.ModelSerializer):
    teams = TeamSerializer()
    class Meta:
        model = TournamentDetail
        fields = ['teams']

class TourneySerializer(serializers.ModelSerializer):
    games = GameSerializer()
    tourney = TourneyDetailSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ['id', 'name', 'games', 'status', 'tourney']