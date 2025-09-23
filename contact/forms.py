from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Enter Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Enter Your Email'
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Enter Your Subject'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'styled-input',
            'placeholder': 'Enter Your Message',
            'rows': 5
        })
    )
