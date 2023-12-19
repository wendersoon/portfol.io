from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    