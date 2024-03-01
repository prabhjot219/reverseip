from django.http import HttpResponse
import socket

def reverse_ip(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
    reversed_ip = '.'.join(socket.gethostbyname(client_ip).split('.')[::-1])
    print("Reversed IP:", reversed_ip)
    return HttpResponse(f"Reversed IP: {reversed_ip}")
