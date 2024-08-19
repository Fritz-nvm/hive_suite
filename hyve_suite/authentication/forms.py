from django.forms import ModelForm
from models import user

class sign_up_form(ModelForm):
    class Meta:
        model = user
        fields = [ 'email', 'password']
        
class login_form(ModelForm):
    class Meta:
        model = user
        fields = [ 'email', 'password']