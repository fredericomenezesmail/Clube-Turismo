from rest_framework import viewsets

from .serializers import ClubeTurismoUserSerializer
from .models import ClubeTurismoUser

class ClubeTurismoUserViewSet(viewsets.ModelViewSet):
    queryset = ClubeTurismoUser.objects.all().order_by('name')
    serializer_class = ClubeTurismoUserSerializer