from django.contrib import admin
from .models import User, Game, Team, Tournament, TournamentDetail

# Register your models here.
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(TournamentDetail)