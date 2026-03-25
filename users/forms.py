from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginUser(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50,label='Usuario',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'username',
                                                             'placeholder': 'Usuario'}))
    password = forms.CharField(required=True,label='Contraseña',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'id': 'password',
                                                             'placeholder': 'Contraseña'}))

class RegistroUsuario(forms.Form):
    
    identificacion = forms.CharField(required=True, min_length=4, max_length=50,label='identificacion',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'identificacion',
                                                             'placeholder': 'identificacion'}))
    
    nombres = forms.CharField(required=True, min_length=4, max_length=50,label='nombres',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'identificacion',
                                                             'placeholder': 'nombres'}))
    
    username = forms.CharField(required=True, min_length=4, max_length=50,label='Usuario',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'username',
                                                             'placeholder': 'Username'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'id': 'password',
                                                             'placeholder': 'Password'}))
    AGENCIA_CHOICES = [
    ('', ''),
    ('MOCOA', 'Mocoa'),
    ('PUERTO ASIS', 'Puerto Asis'),
    ('DORADA', 'Dorada'),
    ('HORMIGA', 'Hormiga'),
    ('ORITO', 'Orito'),
    ('VILLA GARZON', 'Villa Garzon'),
    ('PUERTO LEGUIZAMO', 'Puerto Leguizamo'),
    ('SIBUNDOY', 'Sibundoy'),
]
    agencia = forms.ChoiceField(choices=AGENCIA_CHOICES, required=True, label='agencia',
                                widget=forms.Select(attrs={'class': 'form-control',
                                                           'id': 'agencia',
                                                           'placeholder': 'agencia'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                             'id': 'email',
                                                             'placeholder': 'Email'}))
    
    TIPOS_USUARIO = [
        ('', ''),
        (1, 'Administrador'),
        (2, 'Cliente'),
    ]
    
    is_superuser = forms.ChoiceField(label='Tipo de usuario',required=True,choices=TIPOS_USUARIO,
        widget=forms.Select(attrs={'class': 'form-control','id': 'tipousuario'})  # Personaliza el widget aquí
    )
        
    #usuario no se repita y no genere error
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists() :
            raise forms.ValidationError("el usuario ya se encuentra creado")
        
        return username
    
    #identificacion no se repita y no genere error
    def clean_identificacion(self):
        identificacion = self.cleaned_data.get('identificacion')
        
        if User.objects.filter(identificacion=identificacion).exists() :
            raise forms.ValidationError("El numero de identificacion ya se encuentra creado")
        
        return identificacion
    #Guardar  
    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        identificacion = self.cleaned_data['identificacion']
        nombres = self.cleaned_data['nombres']
        agencia = self.cleaned_data['agencia']
        
        user = User.objects.create_user(username=username, email=email, password=password,
                                        identificacion=identificacion, nombres=nombres, agencia=agencia)

        return user

class CambiarClaveForm(forms.Form):
    passwordActual = forms.CharField(label= 'Contraseña actual',required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'id': 'password',
                                        'placeholder': 'Contraseña actual'}))
    passwordNew = forms.CharField(label= 'Contraseña nueva',required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'passwordNew',
        'placeholder': 'Contraseña nueva'}))
    passwordNewConfirm = forms.CharField(
        label= 'Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'passwordNewConfirm',
            'placeholder': 'Confirmar contraseña'}))