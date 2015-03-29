from .models import Picture
from .serializers import PictureSerializer
from rest_framework import generics


class PictureList(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
