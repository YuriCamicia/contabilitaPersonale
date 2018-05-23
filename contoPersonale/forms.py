from	django	import	forms
from	.models	import	Conto, Transazione
'''
class	managerForm(forms.ModelForm):
    class	Meta:
        model	=	Conto
        fields	=	('nome',)
'''

class managerForm(forms.Form):
    nome = forms.ModelChoiceField(queryset=Conto.objects.all(),empty_label="-- seleziona --")

class sceltaTransazioneForm(forms.Form):
    
   
    def __init__(self, *args, **kwargs):
        super(sceltaTransazioneForm, self).__init__(*args, **kwargs)
        self.fields['periodicita'] = forms.ChoiceField(choices=get_my_choices() )

def get_my_choices():
        # you place some logic here
        FISSA = 'FIS'
        VARIABILE = 'VAR'
        SCELTA_PERIODICITA = (
            (VARIABILE, 'Variabile'),
            (FISSA, 'Fissa'),
        )
        return SCELTA_PERIODICITA