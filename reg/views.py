from django.shortcuts import render



# Create your views here.



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