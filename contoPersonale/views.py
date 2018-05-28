from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Conto, Transazione
from .forms	import	managerForm, sceltaTransazioneForm


def gestione_conto(request, pk):
    conto = get_object_or_404(Conto, pk=pk)
    periodicitaTransazione= 'VAR'
    transazioni = Transazione.objects.filter(conto_ref=conto).filter(periodicita=periodicitaTransazione).order_by('-data')
    if	request.method	==	"POST":
        form2	=	sceltaTransazioneForm(request.POST)
        if	form2.is_valid():
            periodicitaTransazione = form2.cleaned_data['periodicita']
            transazioni = Transazione.objects.filter(conto_ref=conto).order_by('-data')
            transazioni = Transazione.recuperoTransazioniPerPeriodicita(transazioni,periodicitaTransazione)
            #transazioni = transazioni.filter(periodicita=periodicitaTransazione).order_by('-data')
    else:
        form2 = sceltaTransazioneForm()    
    importo_totale = 0
    for transazione in transazioni:
        if(transazione.tipo=='OUT'):
            importo_totale -= transazione.importo
        else:
            importo_totale += transazione.importo
    return render(request,'contoPersonale/gestione_conto.html', { 'conto':conto, 'transazioni':transazioni ,'form2':form2, 'periodicitaTransazione':periodicitaTransazione, 'importo_totale':importo_totale} )


def start(request):
    if	request.method	==	"POST":
        form1	=	managerForm(request.POST)
        
        if	form1.is_valid():
            nomeConto = form1.cleaned_data['nome']
            conto = Conto.objects.get(nome=nomeConto)
            return	redirect('gestione_conto', pk=conto.pk)
    else:
        form1	=	managerForm()
    conti = Conto.objects.all().order_by('nome')
    return render(request,'contoPersonale/start.html', {'conti':conti, 'form1':	form1 } )

