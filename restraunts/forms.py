from django.forms import ModelForm
from .models import restraunt

class CreateRestraunt(ModelForm):
    class Meta:
        model = restraunt
        fields = '__all__'