from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(), max_length=500)
