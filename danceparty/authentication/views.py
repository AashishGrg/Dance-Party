from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View

from .forms import SignUpForm


class UserSignupForm(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user.set_password(password)
            user.is_superuser = False
            user.save()

            # returns these objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # after signup redirect to profile settings
                    return redirect('authentication:login')

        return render(request, self.template_name, {'form': form})


# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dancepartyapp:dashboard')
        else:
            print("Someone tried to login and failed.")
            return redirect('authentication:login')
    else:
        return redirect('authentication:login')


# logout
def logout_view(request):
    logout(request)
    return redirect('authentication:login')
