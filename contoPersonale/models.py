from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

'''
Legenda:
    class Conto:
        tipo = scelta multipla tra conto corrente e risparmio
'''

class Conto(models.Model):
    nome = models.CharField(max_length=200)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    

    CONTO_CORRENTE = 'CC'
    CONTO_RISPARMIO = 'CR'
    SCELTA_TIPO = (
        (CONTO_CORRENTE, 'Conto Corrente'),
        (CONTO_RISPARMIO, 'Conto Risparmio'),
    )
    tipo = models.CharField(
        max_length=2,
        choices=SCELTA_TIPO,
        default=CONTO_CORRENTE,
    )

    def __str__(self):
        return self.nome

    

'''
Legenda:
    class Transazione:
        conto_ref = conto di riferimento alla transazione
        
        tipo = scelta multipla tra in entrata e in uscita
        periodicita = scelta multipla tra fissa e variabile
'''

class Transazione(models.Model):
    importo = models.DecimalField(max_digits=19, decimal_places=2)
    descrizione = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    conto_ref = models.ForeignKey('Conto', on_delete=models.CASCADE)
    
    ENTRATA = 'IN'
    USCITA = 'OUT'
    SCELTA_TIPO = (
        (ENTRATA, 'In Entrata'),
        (USCITA, 'In Uscita'),
    )
    
    tipo = models.CharField(
        max_length=3,
        choices=SCELTA_TIPO,
        default=USCITA,
    )

    FISSA = 'FIS'
    VARIABILE = 'VAR'
    SCELTA_PERIODICITA = (
        (FISSA, 'Fissa'),
        (VARIABILE, 'Variabile'),
    )
    
    periodicita = models.CharField(
        max_length=3,
        choices=SCELTA_PERIODICITA,
        default=VARIABILE,
    )

    
    def recuperoTransazioniPerPeriodicita(paramTransazione,paramPeriodicita):
        #filtro gli oggeti transazione in base alla periodicità
        transazione = paramTransazione.filter(periodicita=paramPeriodicita).order_by('-data')
        return transazione

    def __str__(self):
        return self.descrizione


@receiver(post_save, sender=Transazione)
def salva_nuova_transazione(sender, **kwargs):
    if kwargs.get('created', False):
        instance = kwargs.get('instance')
        #prendo il riferimento al conto per pk
        conto_rifer = Conto.objects.get(pk = instance.conto_ref.id )
        #aggiorno il saldo in base al tipo di transazione
        if(instance.tipo=='OUT'):
            conto_rifer.saldo -= instance.importo
        else:
            conto_rifer.saldo += instance.importo
        #salvo il nuovo saldo della classe conto
        conto_rifer.save()

'''
Post save seconda implementazione

@receiver(post_save, sender=Transazione)
def salva_nuova_transazione(sender, **kwargs):
    if kwargs.get('created', False):
        instance = kwargs.get('instance')
        #prendo il riferimento al conto per pk
        conto_rifer = Conto.objects.get(pk = instance.conto_ref.id )
        transazioni = Transazione.objects.filter(conto_ref=conto)
        #aggiorno il saldo in base al tipo di transazione
        importo_totale = 0
        for transazione in transazioni:
            if(transazione.tipo=='OUT'):
                importo_totale -= transazione.importo
            else:
                importo_totale += transazione.importo
        #salvo il nuovo saldo della classe conto
        conto_rifer.tot_transazioni = importo_totale
        conto_rifer.save()
'''

@receiver(pre_delete, sender=Transazione)
def elimina_transazione(sender, **kwargs):
    instance = kwargs.get('instance')
    #prendo il riferimento al conto per pk
    conto_rifer = Conto.objects.get(pk = instance.conto_ref.id )
    #riassegno il saldo prima dell'eliminazione della transazione in base al tipo
    #se OUT incremento il saldo
    #se IN decremento il saldo
    if(instance.tipo=='OUT'):
        conto_rifer.saldo += instance.importo
    else:
        conto_rifer.saldo -= instance.importo
    #salvo il nuovo saldo della classe conto
    conto_rifer.save()



'''

@receiver(pre_save, sender=Transazione)
def modifica_transazione(sender, **kwargs):
    instance = kwargs.get('instance')
    
    #prendo il riferimento al conto per pk
    conto_rifer = Conto.objects.get(pk = instance.conto_ref.id )
    #riassegno il saldo prima della modifica della transazione in base al tipo
    #se OUT incremento il saldo
    #se IN decremento il saldo
    if(instance.tipo=='OUT'):
        conto_rifer.saldo += instance.importo
    else:
        conto_rifer.saldo -= instance.importo
    #salvo il nuovo saldo della classe conto
    conto_rifer.save()
'''
