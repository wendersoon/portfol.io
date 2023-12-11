from django.urls import path, include
from .views import IndexView, RegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),


]