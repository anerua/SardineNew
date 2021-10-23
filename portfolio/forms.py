from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=64, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=64, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_address = forms.EmailField(label='Your Email', max_length=64, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your Message', max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    