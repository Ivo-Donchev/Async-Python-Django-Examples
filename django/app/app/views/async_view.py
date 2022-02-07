# type: ignore
from asgiref.sync import sync_to_async

from django.http import HttpResponse
from django.contrib.auth.models import User


COUNTER = 0


@sync_to_async
def func():
    return list(User.objects.all())


async def async_view(self):
    res = []

    for user in range(1000):
        res.append(await func())

    return HttpResponse(f"Result: {res}")
