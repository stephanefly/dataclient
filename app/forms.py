from django import forms
from .models import FormulaireEvenement

class DateInput(forms.DateInput):
    input_type = 'date'

class FormulaireEvenementForm(forms.ModelForm):
    class Meta:
        model = FormulaireEvenement
        fields = '__all__'
        widgets = {
            'date_event': DateInput(),
        }

    salle = forms.CharField(required=False)
    photobooth = forms.ChoiceField(choices=FormulaireEvenement.PHOTOBOTH_CHOICES, required=False)
    commentaire = forms.CharField(required=False)