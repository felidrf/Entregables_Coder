from django import forms

class FamiliaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    fecha=forms.DateField()

class DeportesFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    jugadores=forms.IntegerField()

class EquiposFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    medallas=forms.IntegerField()



