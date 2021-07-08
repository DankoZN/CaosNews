from django import forms
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaborador


class ColaboradorForm (forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = ['rutColaborador', 'nomColaborador','imagen', 'fonoColaborador',
        'dirColaborador', 'emailColaborador', 'paisColaborador', 'contrasenaColaborador']
        labels ={
            'rutColaborador': 'Rut',  
            'imagen': 'Imágen',
            'nomColaborador': 'Nombre', 
            'fonoColaborador': 'Teléfonor',
            'dirColaborador': 'Dirección',
            'emailColaborador': 'E-mail',
            'paisColaborador': 'País',
            'contrasenaColaborador': 'Contraseña',

        }
        widgets={
            'rutColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rutColaborador'
                }
            ), 
            'imagen': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                'id': 'imagen','name': 'imagen',
                'accept':"imagen/*"}
            ),
            'nomColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nomColaborador'
                }
            ), 
            'fonoColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese teléfono', 
                    'id': 'fonoColaborador'
                }
            ), 
            'dirColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección',
                    'id': 'dirColaborador',
                }
            ),
            'emailColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su E-Mail',
                    'id': 'emailColaborador',
                }
            ),
            'paisColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el país',
                    'id': 'paisColaborador',
                }                
            ),
            'contrasenaColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña',
                    'id': 'contrasenaColaborador',
                }
            )          

        }