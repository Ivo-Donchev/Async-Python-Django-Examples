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
    """
    Pros:
        - allows scaling by CPU
    Cons:
        - It's just slow
        - Impossible for Django to tell you for "flying processes"
        - Impossible retry mechanism
        - Unusable for GET requests (SELECT)
        - We already have a tool for that - Celery
    """
    processes = []

    for i in range(6):
        process = multiprocessing.Process(target=func)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    return HttpResponse('Done')
