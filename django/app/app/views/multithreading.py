import threading

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User


def func():
    # ORM operation
    print(User.objects.all())

    # CPU Operation
    for i in range(100000000):
        pass


def view_with_threading(request):
    threads = []

    for i in range(6):
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return HttpResponse('Done')
