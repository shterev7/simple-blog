from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm


def home(request):
        digits = [0,1,2,3,4,5,6,7,8,9]
        name = 'Stoyan Shterev'

        args = {'myname': name, 'digits': digits}
        return render(request,'personal/home.html', args)
        
def register(request):
        form = RegistrationForm(request.POST or None)
        if request.method=='POST':      
                if form.is_valid():
                        form.save()
                        return redirect('/account')
        else:
                form = RegistrationForm()

                args = {'form': form}
                return render(request,'accounts/reg_form.html',args)
