from .models import Message, ViewsCounter

def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def count_views(message, client_ip):
    seen = len(ViewsCounter.objects.filter(message=message, ip=client_ip))
    if seen == 0:
        ViewsCounter.objects.create(message=message, ip=client_ip)

    return len(ViewsCounter.objects.filter(message=message))
