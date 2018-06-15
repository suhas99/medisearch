from django.shortcuts import render, render_to_response, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User  
from django.views import generic
from django.views.generic import View

# Create your views here.
from .forms import UserForm
from medicine.models import MedicalShop , Products ,Type


def register_user(request):
 if request.user.is_authenticated():
      return HttpResponseRedirect('/user/')
  else:
      if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
            if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')

        context = {}
        context.update(csrf(request))
        context['form'] = MyRegistrationForm()

        return render(request, 'register.html', context)


class UserFormView(View):
 form_class = UserForm
 template_name =  'register.html'

 def get(self,request):
  form = self.form_class(None)
  return render(request,self.template_name,{'form':form})

 def post(self,request):
  form =self.form_class(request.POST) 

  if form.is_valid():
   #User = get_user_model()
   user = form.save(commit=False)
   username = form.cleaned_data['username']
   password = form.cleaned_data['password']
   email = form.cleaned_data['email']
   user.set_password(password)
   user.is_staff = True
   user = User.objects.create_user(username,password,email)
   user.save()
   user = authenticate(username=username, password=password)

   if user is not None:
    if user.is_active:
     is_staff=True
     login(request, user)
     return redirect('/admin/')
  return render(request,self.template_name,{'form':form})









	
