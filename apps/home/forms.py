from django import forms
from apps.home.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'address', 'phone', 'role',)
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'form-control'