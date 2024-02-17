from django import forms
from .models import Categoria, Plato

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre Categoria',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la categoría'}),
        max_length=50,
        required=True,
        help_text='Ingrese el nombre de la categoría.',
        error_messages={'required': 'El campo de Nombre es obligatorio.'}  # Mensaje personalizado para campos requeridos
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener todas las categorías y sus órdenes
        categorias = Categoria.objects.all().order_by('orden')
        # Generar una lista de tuplas (valor, etiqueta) para el campo 'orden'
        opciones_orden = [(categoria.orden, categoria.orden) for categoria in categorias]
        # Agregar una opción adicional para el caso de una nueva categoría
        ultimo_orden = categorias.order_by('-orden').first()
        if ultimo_orden:
            opciones_orden.append((ultimo_orden.orden + 1, ultimo_orden.orden + 1))
        else:
            opciones_orden.append((1, 1))
        # Asignar las opciones al campo 'orden'
        self.fields['orden'] = forms.ChoiceField(choices=opciones_orden, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.strip() == '':
            raise forms.ValidationError("El nombre no puede consistir solo de espacios en blanco.")
        return nombre

    class Meta:
        model = Categoria
        fields = ['nombre', 'orden']

class CategoriaCrearForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre Categoria',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la categoría'}),
        max_length=50,
        required=True,
        help_text='Ingrese el nombre de la categoría.',
        error_messages={'required': 'El campo de Nombre es obligatorio.'}  # Mensaje personalizado para campos requeridos
    )


    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.strip() == '':
            raise forms.ValidationError("El nombre no puede consistir solo de espacios en blanco.")
        return nombre

    class Meta:
        model = Categoria
        fields = ['nombre']

#Form para Plato
class PlatoForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre Plato',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del plato'}),
        max_length=50,
        required=True,
        help_text='Ingrese el nombre del plato.',
        error_messages={'required': 'El campo de Nombre es obligatorio.'}  # Mensaje personalizado para campos requeridos
    )
    descripcion = forms.CharField(
        label='Descripcion',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del plato'}),
        max_length=50,
        required=True,
        help_text='Ingrese la descripcion.',
        error_messages={'required': 'El campo de descripcion es obligatorio.'}  # Mensaje personalizado para campos requeridos
    )
    precio = forms.IntegerField(
        label='Precio',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}),
        required=True,
        help_text='Ingrese el precio.',
        error_messages={'required': 'El campo de precio es obligatorio.'}  # Mensaje personalizado para campos requeridos
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione una categoria"  # Agrega esta línea para mostrar un texto por defecto en el select
    )

    

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.strip() == '':
            raise forms.ValidationError("El nombre no puede consistir solo de espacios en blanco.")
        return nombre

    class Meta:
        model = Plato
        fields = ['nombre', 'descripcion','precio','categoria']   




