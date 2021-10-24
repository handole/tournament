from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid')
    status = models.BooleanField(default=False)
    id_games = models.ForeignKey(Game, on_delete=models.DO_NOTHING, related_name='id_game')
    
    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100) # ('regis open', 'finished')
    games = models.ForeignKey(Game, on_delete=models.DO_NOTHING, related_name='games')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class TournamentDetail(models.Model):
    tourney = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tourney')
    teams = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='teams')
    