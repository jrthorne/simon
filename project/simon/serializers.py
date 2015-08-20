from rest_framework import serializers
from simon.models import Player

# allows REST updates to a player during game play.
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'high_score')
    # end Meta
# end PlayerSerializer

