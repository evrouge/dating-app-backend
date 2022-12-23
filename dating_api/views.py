from rest_framework import generics
from .serializers import DatingSerializer
from .models import Dating

# Create your views here.
class DatingList(generics.ListCreateAPIView):
    queryset = Dating.objects.all().order_by('id')
    serializer_class = DatingSerializer

class DatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dating.objects.all().order_by('id')
    serializer_class = DatingSerializer
