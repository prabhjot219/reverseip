from django.http import HttpResponse
import socket
from reverse_ip_app.models import ReversedIP

def reverse_ip(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
    reversed_ip = '.'.join(socket.gethostbyname(client_ip).split('.')[::-1])
    try:
        ReversedIP.objects.create(original_ip=client_ip, reversed_ip=reversed_ip)
    except Exception as e:
        pass
    print("Reversed IP:", reversed_ip)
    return HttpResponse(f"Reversed IP: {reversed_ip}")
