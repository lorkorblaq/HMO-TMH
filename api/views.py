from django.shortcuts import render
from rest_framework import generics
from .models import Hospitals
from .serializers import HospitalsSerializer

class HospitalsList(generics.ListCreateAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializer

class HospitalsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializer