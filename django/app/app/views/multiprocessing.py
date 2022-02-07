import multiprocessing

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User


def func():
    # ORM operation
    print(User.objects.all())

    # CPU Operation
    for i in range(100000000):
        pass


def view_with_multiprocessing(request):
    processes = []

    for i in range(6):
        process = multiprocessing.Process(target=func)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    return HttpResponse('Done')
