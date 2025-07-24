from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['resena']                            
        labels = {
            'resena': 'Tu Reseña', 
        }
        widgets = {
            'resena': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribí tu reseña acá...'}),
        }
