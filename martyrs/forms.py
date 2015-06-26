from django import forms
from .models import Martyr

class MartyrForm(forms.ModelForm):
    class Meta:
        model = Martyr
        fields = [ 'name' , 'date_of_birth' , 'date_of_death' , 'cause_of_death', 'officer_name', 'governorate']