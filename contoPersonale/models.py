from django.db import models
from django.utils import timezone

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

    '''
    def filtroTransazioniPeriodicita(self,paramPeriodicita, paramContoRef):
        #filtro le transazioni che si riferiscono al conto per pk
        transazioni=self.objects.filter(conto_ref=paramContoRef)
        #filtro gli oggeti transazione in base alla periodicità
        if(paramPeriodicita=='VAR'):
            transazioni = self.objects.filter(self.periodicita=='VAR')
        else:
            transazioni = self.objects.filter(self.periodicita=='FIS')

        for transazione in transazioni:
            print('importo: '+transazione.importo)
            print('descrizione: '+transazione.descrizione)
            print('data: '+transazione.data)
            print('tipo: '+transazione.tipo)
    '''
    
    def save(self,*args, **kwargs):
        #prendo il riferimento al conto per pk
        conto_rifer = Conto.objects.get(pk = self.conto_ref.id )
        #aggiorno il saldo in base al tipo di transazione
        if(self.tipo=='OUT'):
            conto_rifer.saldo -= self.importo
        else:
            conto_rifer.saldo += self.importo
        #salvo il nuovo saldo della classe conto
        conto_rifer.save()
        #salvo la classe transazione
        super(Transazione, self).save(*args, **kwargs)

    def __str__(self):
        return self.descrizione


    