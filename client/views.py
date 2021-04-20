from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import Client, Service

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_ur = reverse_lazy('login')
    template_name = 'registration/signup.html'

""" def client_list(request):
    clients = Client.objects.all()
    services = Service.objects.all()

    return render(
        request, 
        'templates/client_list.html',
        {
            'client': clients,
            'service': services
        }
    )
 """
# Create your views here.
