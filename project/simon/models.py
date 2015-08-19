#################################################################
FileName        = 'models.py'
# By:            Jason Thorne
# Date:            19-08-2015
# Description:     The simon project
##################################################################
import datetime, pytz
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max, Min, Q 
from django.http import Http404

# Create your models here.
class Player(models.Model):
	# one to one with django user. You can select any user to be a player 
	user = models.OneToOneField(User)
	games_played