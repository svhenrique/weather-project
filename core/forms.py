from django import forms
from .models import Location
from .validators import validate_location

class FacadeForm(forms.Form):
    """
    Facade class for Location model. This class have the values for Location model
    in just one field.
    """
    location = forms.CharField(label='Lugar', max_length=310, required=True, validators=[validate_location],
                            widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Lugar'}))


