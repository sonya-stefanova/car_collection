import email

from car_collection.web.models import Profile, Car
from django import forms




class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

class ProfileEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance



class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')

class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')

class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.disabled = True





