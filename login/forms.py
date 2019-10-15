"""forms.py for login"""
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    """form for user"""
    """https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name"""
    class Meta:
        model = User
        fields = (
            'user_name',
            'user_email',
            'user_mobile',
            'user_dob',
            'user_description'
        )
        labels = {
            'user_name':'Name',
            'user_email':'Email',
            'user_mobile':'Mobile',
            'user_dob':'DOB',
            'user_description':'Description'
        }
        """http://www.learningaboutelectronics.com/Articles/How-to-create-a-date-field-in-a-Django-form.php"""
        attributes = { 'class':'form-control',}
        YEARS = [x for x in range(1940, 2020)]
        widgets = {
            'user_name':forms.TextInput(attrs=attributes),
            'user_email':forms.TextInput(attrs=attributes),
            'user_mobile':forms.TextInput(attrs=attributes),
            'user_dob':forms.SelectDateWidget(years=YEARS),
            'user_description':forms.TextInput(attrs=attributes)
        }
