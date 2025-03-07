from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserLoginForm, UserRegisterForm


class UserRegisterView(CreateView):
    """
    View to register new user
    """
    template_name = 'user_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('projects:home')

    def form_valid(self, form):
        user = form.save(commit=False)  # Getting user from Form
        user.is_active = True  # Active user
        user.save()  # Saving user

        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(self.request, email=email, password=raw_password)

        if user is not None:
            login(self.request, user)

        return redirect(self.success_url)


class LoginUserView(LoginView):
    """
    User Login View
    """
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            # raise (f"welcome {self.request.user} !")
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Invalid email or password")
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("projects:home")


# User Logout functions
def user_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'user_logout.html')



