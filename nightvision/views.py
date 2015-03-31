from .models import Picture
from .serializers import PictureSerializer
from rest_framework import generics
from rest_framework import permissions


class PictureList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
