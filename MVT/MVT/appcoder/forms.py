from django import forms

class FamiliaFormulario(forms.Form):

    nombre=forms.CharField()
    edad=forms.IntegerField()
    fecha=forms.DateField()


class DeportesFormulario(forms.Form):

    nombre=forms.CharField()
    jugadores=forms.IntegerField()


class EquiposFormulario(forms.Form):

    nombre=forms.CharField()
    medallas=forms.IntegerField()



