from django import forms

from members.models import Member

class MemberCreationForm(forms.ModelForm):
    
    
    class Meta:
        model = Member
        exclude = ('id',)
        
    
        error_messages = {
            "last_name": {
                "required": "Please enter last name."
            },
        }
        
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),
            "age": forms.NumberInput(attrs={
                "placeholder": "Enter your age"
            }),
            "phone": forms.NumberInput(attrs={
                "placeholder": "Enter your phone"
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].error_messages['required'] = 'Please enter first name'
        
        
        