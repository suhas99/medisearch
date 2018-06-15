from django.contrib.auth.models import User
from django import forms




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        #user.name = self.cleaned_data['name']

        if commit:
            user.save()

        return user 






   # def save(self, commit=True):
   #     user = super(MyRegistrationForm, self).save(commit=False)
    #    user.email = self.cleaned_data['email']
     #   user.name = self.cleaned_data['name']

      #  if commit:
       #     user.save()

        #return user