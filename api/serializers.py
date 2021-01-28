from rest_framework import serializers

from .models import ClubeTurismoUser

class ClubeTurismoUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClubeTurismoUser
        fields = ('name', 'alias')