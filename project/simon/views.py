from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from json import dumps
from .serializers import PlayerSerializer
from rest_framework import generics
from .models import *


# Create your views here.
@ensure_csrf_cookie
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
    """
    Retrieve update or delete a player instance
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def post(self, context, **response_kwargs):
        myID = int(self.request.POST.get('id', None))
        high_score = int(self.request.POST.get('id', None))
        thisPlayer = get_object_or_404(Player, pk=myID)
        # increment the number of games played
        thisPlayer.games_played += 1
        if high_score > thisPlayer.high_score:
            thisPlayer.high_score = high_score
        # end if
        thisPlayer.save()

        response = {'id': myID, 'high_score': high_score}
        return HttpResponse(dumps(response))
    # end post

    def perform_update(self, serializer):
        # this is probably a bad way to do this, but I just want to get it working
        thisPlayer = get_object_or_404(Player, pk=self.kwargs.get('pk'))
        # increment the number of games played
        thisPlayer.games_played += 1
        thisPlayer.save()

        # check that the high score passed is higher than existing
        if serializer.data.get('high_score', 0) > thisPlayer.high_score:
            instance = serializer.save()
        # end if
    # end perform_update

# end PlayerDetail

class PlayerListView(ListView):
    model = Player
    template_name = 'simon/high_scores.html'

# end PlayerListView