from ..models import Conto, Transazione
from rest_framework import serializers


class ContoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conto
        fields = ('nome', 'saldo_iniziale', 'tot_transazioni', 'saldo_attuale' , 'url')

class TransazioneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transazione
        fields = ('importo', 'descrizione', 'data', 'conto_ref', 'tipo', 'periodicita', 'url')


