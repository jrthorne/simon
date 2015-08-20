from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .serializers import PlayerSerializer
from rest_framework import generics
from .models import *


# Create your views here.
def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('simon/home.html',
                             context_instance=context)
# end home

# For returning list in JSON format. Not really required at this stage
class PlayerList(generics.ListCreateAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

# end PlayerList

# Will need this to update the player's high score and number of games played
# using an AngularJS call
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

# end PlayerDetail

class PlayerListView(ListView):
  model = Player
  template_name = 'simon/high_scores.html'

# end PlayerListView