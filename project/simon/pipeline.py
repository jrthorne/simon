from django.contrib import auth
from social.apps.django_app.default.models import UserSocialAuth
from social.exceptions import AuthAlreadyAssociated
from django.contrib.auth.models import User
from simon.models import Player

# Any social auth cretaed user should be a player
def create_player(backend, details, response, user=None, *args, **kwargs):
    if user and user.pk:
        try:
            oldPlayer = user.player
        except Player.DoesNotExist:
            # User exists, player does not. Create player
            newPlayer = Player(user=user)
            newPlayer.save()
        # end try
        
        return {
            'user': user,
            'is_new': False,
        }
    else:
        
        return {
            'user': user,
            'is_new': False,
        }
    # endif
# end create_player