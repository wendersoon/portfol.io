from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    
class PortfolioView(TemplateView):
    
    template_name = 'portfolio.html'
    
class RegisterView(CreateView):
    
   form_class = UserCreationForm
   template_name = 'register.html'
   success_url = reverse_lazy('login')
