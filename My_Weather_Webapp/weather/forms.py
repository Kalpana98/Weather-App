from django.forms import ModelForm, TextInput
from .models import City 

class CityForm(ModelForm):
    class Meta:
<<<<<<< HEAD
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
=======
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
>>>>>>> f518a7a5c6daffbf8b292f6c03d935baa118e61d
