from django.http import HttpResponse


def view_with_multiprocessing(request):
    return HttpResponse('Done')
