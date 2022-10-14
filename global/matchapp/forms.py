from django import forms
from matchapp.models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'