from django import forms
from .models import Sesion, Asistente

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'

class AsistenteForm(forms.ModelForm):
    class Meta:
        model = Asistente
        fields = '__all__'

class ArchivoForm(forms.Form):
    archivo = forms.FileField(label='Cargar archivo')