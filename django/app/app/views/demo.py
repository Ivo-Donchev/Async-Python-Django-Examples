import asyncio

from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.contrib.auth.models import User


def demo(request):
    return HttpResponse('Done')


async def sleeping():
    print('Sleep...')
    await asyncio.sleep(2)
    print('Wake up...')
    return await sync_to_async(User.objects.first)()


async def demo_async(request):
    users = await asyncio.gather(
        *[
            sleeping()
            for i in range(100)
        ]
    )
    print(users)

    return HttpResponse('Done')
