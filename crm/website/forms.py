from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email Address"}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}))
    email = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"email"}))
    phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"phone"}))
    # last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}))
    # last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name","email", "phone",)


    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields['phone'].widget.attrs['class'] = 'form-control'
        # self.fields['phone'].widget.attrs['placeholder'] = 'User Name'
        # self.fields['phone'].label = ''
        # self.fields['phone'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # self.fields['country1'].widget.attrs['class'] = 'form-control'
        # self.fields['country1'].widget.attrs['placeholder'] = 'country'
        # self.fields['country1'].label = ''
        # self.fields['country1'].help_text = '<ul class="form-text text-muted small"><li>Your country can\'t be too similar to your other personal information.</li><li>Your country must contain at least 8 characters.</li><li>Your country can\'t be a commonly used country.</li><li>Your country can\'t be entirely numeric.</li></ul>'

        # self.fields['country2'].widget.attrs['class'] = 'form-control'
        # self.fields['country2'].widget.attrs['placeholder'] = 'Confirm country'
        # self.fields['country2'].label = ''
        # self.fields['country2'].help_text = '<span class="form-text text-muted"><small>Enter the same country as before, for verification.</small></span>'	
