# events/forms.py

from django import forms
from .models import Event, Registration

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'category']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []
