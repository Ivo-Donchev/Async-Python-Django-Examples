from django.http import HttpResponse


def demo(request):
    return HttpResponse('Done')

def async_demo(request):
    return HttpResponse('Done')
