from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from users.forms import UserSignInForm, UserSignUpForm


class SignInView(LoginView):
    form_class = UserSignInForm
    template_name = 'users/signin.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Войти'
        return context


class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signin')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Регистрация'
        return context
