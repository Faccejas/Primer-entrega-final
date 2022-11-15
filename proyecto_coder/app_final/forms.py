from django import forms

class NuestrosclientesFormulario(forms.Form):

    nombre = forms.CharField()
    categoria = forms.CharField()