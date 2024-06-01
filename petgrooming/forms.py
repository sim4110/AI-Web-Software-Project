from django import forms
from .models import StoreData

class StoreDataForm(forms.ModelForm):
    class Meta:
        model = StoreData
        fields = ['writer', 'writetime', 'store_name', 'store_owner', 'tel_num', 'anesthesia', 'location', 'opentime', 'closetime', 'qualifications', 'store_image']
        widgets = {
            'opentime': forms.TimeInput(format='%H:%M'),
            'closetime': forms.TimeInput(format='%H:%M'),
        }
