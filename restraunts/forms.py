from django.forms import ModelForm
from .models import restraunt

class CreateRestraunt(ModelForm):
    class Meta:
        model = restraunt
        fields = ['name','reg_id','contact_no','email_id']