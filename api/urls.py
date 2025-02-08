from django.urls import path
from .views import HospitalsList, HospitalsDetail

urlpatterns = [
    path('hospitals/', HospitalsList.as_view(), name='hospitals_list'),
    path('hospitals/<int:pk>/', HospitalsDetail.as_view(), name='hospitals_detail'),

]