from django.shortcuts import render
from ..models import Conto, Transazione
from rest_framework import viewsets
from contoPersonale.appDRF.serializers import ContoSerializer, TransazioneSerializer


class ContoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Conto to be viewed or edited.
    """
    queryset = Conto.objects.all().order_by('nome')
    serializer_class = ContoSerializer

class TransazioneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Conto to be viewed or edited.
    """
    queryset = Transazione.objects.all().order_by('-data')
    serializer_class = TransazioneSerializer