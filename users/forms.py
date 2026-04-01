from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import User

# Formulario de inicio de sesión
class LoginUser(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50,label='Usuario',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'username',
                                                             'placeholder': 'Usuario'}))
    password = forms.CharField(required=True,label='Contraseña',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'id': 'password',
                                                             'placeholder': 'Contraseña'}))
# Formulario de registro de usuario
class RegistroUsuarioForm(forms.Form):
    
    identificacion = forms.CharField(required=True, min_length=4, max_length=50,label='identificacion',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'identificacion',
                                                             'placeholder': 'identificacion'}))
    
    nombres = forms.CharField(required=True, min_length=4, max_length=50,label='nombres',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'nombres',
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

# Formulario para editar perfil de usuario utilizando ModelForm
class EditarPerfilForm(forms.ModelForm):

    AGENCIA_CHOICES = [
        ('MOCOA', 'Mocoa'),
        ('PUERTO ASIS', 'Puerto Asis'),
        ('DORADA', 'Dorada'),
        ('HORMIGA', 'Hormiga'),
        ('ORITO', 'Orito'),
        ('VILLA GARZON', 'Villa Garzon'),
        ('PUERTO LEGUIZAMO', 'Puerto Leguizamo'),
        ('SIBUNDOY', 'Sibundoy'),
    ]

    TIPOS_USUARIO = [
        (1, 'Administrador'),
        (2, 'Cliente'),
    ]

    agencia = forms.ChoiceField(
        choices=AGENCIA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    is_superuser = forms.CharField(
        label='Tipo de usuario',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'style': 'background-color: #e9ecef; cursor: not-allowed;'
        })
    )

    class Meta:
        model = User
        # Especificamos los campos que queremos mostrar en el formulario
        fields = [
            'identificacion',
            'nombres',
            'username',
            'agencia',
            'email',
        ]
        # Personalizar los nombres de los Labels
        labels = {
            'username': 'Usuario',
            'email': 'Email',
            'is_superuser': 'Tipo de usuario',
        }
        # Personalizar los widgets para cada campo
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
             'username': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'style': 'background-color: #e9ecef; cursor: not-allowed;'
            }),
            #'agencia': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'is_superuser': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
    
    # VALIDACIÓN PERSONALIZADA PARA IDENTIFICACIÓN
    def clean_identificacion(self):
        identificacion = self.cleaned_data.get('identificacion')
        # Buscamos si existe otro usuario con esa ID, excluyendo al usuario actual (self.instance)
        if User.objects.filter(identificacion=identificacion).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Erro el número de identificación ya existe en el sistema.")
        return identificacion

     #  Inicializar valores
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields['username'].initial = self.instance.username
            self.fields['is_superuser'].initial = (
                'Administrador' if self.instance.is_superuser else 'Cliente'
            )

    # PROTECCIÓN BACKEND
    def clean_username(self):
        return self.instance.username

    def clean_is_superuser(self):
        return 'Administrador' if self.instance.is_superuser else 'Cliente'

# Formulario para cambiar contraseña
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