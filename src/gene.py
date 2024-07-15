from time import sleep
import time

# def some_fun():
#     for i in range(2):
#         sleep(2)
#         return 1
#
#
# def some_gen_fun_2():
#     for i in range(1, 5):
#         yield 1
#
#
# def some_gen_fun_1():
#     for j in range(2):
#         print(j)
#         some_value = yield from some_gen_fun_2()
#         print(some_value)
#
#
# print(some_fun())

#
# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')
#
#
# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')
#
#
# def main():
#     fun1(4)
#     fun2(4)
#
#
# print(time.strftime('%X'))
#
# main()
#
# print(time.strftime('%X'))

# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def fun3(x):
#     print(x**0.5)
#     await asyncio.sleep(2)
#     print('fun3 завершена')
#
#
# async def fun4(x):
#     print(x**2)
#     await asyncio.sleep(1)
#     print('fun4 завершена')
# print(time.strftime('%X'))
#
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(fun1(4))
# task2 = loop.create_task(fun2(4))
# task3 = loop.create_task(fun3(4))
# task4 = loop.create_task(fun4(4))
# loop.run_until_complete(asyncio.wait([task1, task2, task3, task4]))
#
# print(time.strftime('%X'))

# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

import asyncio
import time
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))
