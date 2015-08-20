#################################################################
FileName        = 'models.py'
# By:            Jason Thorne
# Date:            19-08-2015
# Description:     The simon project
##################################################################
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max, Min, Q 
from django.http import Http404

# Create your models here.
class Player(models.Model):
    # one to one with django user. You can select any user to be a player 
    user = models.OneToOneField(User, related_name='player')
    games_played = models.IntegerField(default=0)
    high_score = models.IntegerField(default=0)

    class Meta:
        ordering = ('high_score',)
    # end Meta

    def __str__(self):
        return str(self.id) + ': ' + self.user.first_name + ': ' + \
            self.user.social_auth.all()[0].provider
    # end __str__
# end Player

