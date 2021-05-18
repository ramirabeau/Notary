from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from .models import Client, Service

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_ur = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HomePageView(ListView):
    model = Client
    template_name = 'home.html'

context_object_name = 'all_client_list'

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
