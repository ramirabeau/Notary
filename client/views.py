from django.shortcuts import render
from .models import Client, Service

def client_list(request):
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

# Create your views here.
