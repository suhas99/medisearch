from registration.forms import RegistrationForm

from mycustomuserapp.models import MyCustomUser



class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = {'name', 'username', 'password1', 'password2', 'email'}

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']

        if commit:
            user.save()

        return user