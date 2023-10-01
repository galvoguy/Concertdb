from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')#"__all__" is an option
        labels = {
                    'name': '',
                   'event_date':'', 
                   'venue': '',
                   'manager': '',
                   'description': '',
                   'attendees':'',}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Event Name'}),
                   'event_date':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Event Date' }), 
                   'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
                   'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
                   'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                   'attendees':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),}


#Create a Venue entry form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address',)#"__all__" is an option
        labels = {
                    'name': '',
                   'address':'', 
                   'zip_code': '',
                   'phone': '',
                   'web': '',
                   'email_address':'',}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Venue Name'}),
                   'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address' }), 
                   'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
                   'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
                   'email_address':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),}
