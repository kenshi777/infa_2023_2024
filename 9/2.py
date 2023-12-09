from collections import namedtuple
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(session, service):
    async with session.get(service.url) as response:
        data = await response.json()
        return service.name, data.get(service.ip_attr, None)

async def asynchronous():
    async with aiohttp.ClientSession() as session:
        # Создание футур для сервисов
        futures = [fetch_ip(session, service) for service in SERVICES]

        # Использование FIRST_COMPLETED
        done, pending = await asyncio.wait(futures, return_when=FIRST_COMPLETED)

        # Получение результата первого завершенного запроса
        for task in done:
            service_name, ip = task.result()
            if ip:
                print(f'{service_name} returned IP: {ip}')
                break
        else:
            print("No service returned a valid IP.")

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
