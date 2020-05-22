from django import forms
from .models import Obra, Images_model
from django.forms import ClearableFileInput

class ObrasForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['fecha_ref','titulo','descripcion','cliente','ubicacion','cover_img']
    # fecha_ref = forms.DateField()
    # titulo = forms.CharField(max_length=20)
    # descripcion = forms.CharField()
    # cliente =  forms.CharField(max_length=20)
    # ubicacion = forms.CharField(max_length=50)
    # myfile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
class ImagenesForm(forms.ModelForm):
    class Meta:
        model= Images_model
        fields = ['img']
        widgets = {
            'img': ClearableFileInput(attrs={'multiple': True}),
        }     
