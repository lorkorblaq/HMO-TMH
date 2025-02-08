from rest_framework import serializers
from .models import Hospitals

class HospitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = '__all__'