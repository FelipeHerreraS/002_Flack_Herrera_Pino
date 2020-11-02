from django import forms

from . models import Peticiones

class PeticionesForm(forms.ModelForm):
    usuario = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    nomAnime =forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))

    class Meta:
        model = Peticiones
        fields = ('usuario','email', 'nomAnime')