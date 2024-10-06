# import requests

# # i/o bound
# response = requests.get('https://github.com/django')

# # cpu-bound
# header_items = response.headers.items()

# # cpu-bound
# res_headers = [f'{key}: {value}' for key, value in header_items]

# # cpu-bound
# formatted_headers = '\n'.join(res_headers)

# # i/o-bound
# with open('headers.txt', 'w') as file:
#     file.write(formatted_headers)


# def function():
#     print('function')

# async def coroutine():
#     print('coroutine')

# import asyncio
# import time

# async def delay(delay_time):
#     print(f'{time.ctime()}: coroutine started.')
#     await asyncio.sleep(delay_time)
#     print(f'{time.ctime()}: coroutine finished.')

# async def main():
#     delay_2 = asyncio.create_task(delay(2))
#     delay_3 = asyncio.create_task(delay(3))

#     await delay_2
#     await delay_3

# asyncio.run(main())


import asyncio
import time

async def fetch_data(url):
    process = await asyncio.create_subprocess_shell(f'curl "{url}"')
    await process.wait()

    if process.returncode == 0:
        print('url: ', process.stdout)

async def main():
    slug_list = [
        "If-we-quantify-the-alarm-we-can-get-to-the-FTP-pixel-through-the-online-SSL-interface!-120863",
        "Try-to-transmit-the-HTTP-card-maybe-it-will-override-the-multi-byte-hard-drive!-120863",
        "Try-to-generate-the-TCP-bus-maybe-it-will-override-the-neural-bandwidth!-120863",
        "You-cant-transmit-the-firewall-without-copying-the-1080p-SDD-interface!-120863",
        "You-cant-connect-the-interface-without-programming-the-virtual-PNG-protocol!-120863",
        "Try-to-bypass-the-SAS-card-maybe-it-will-transmit-the-solid-state-system!-120863",
        "Use-the-auxiliary-EXE-monitor-then-you-can-hack-the-haptic-port!-120863",
    ]
    tasks = [fetch_data(f'https://api.realworld.io/api/articles/{slug}') for slug in slug_list]
    time0 = time.perf_counter()
    await asyncio.gather(*tasks)
    time1 = time.perf_counter()
    print(time1 - time0)

asyncio.run(main())


# import time
# import requests

# def fetch_data(url):
#     return requests.get(url)

# def main():
#     slug_list = [
#         "If-we-quantify-the-alarm-we-can-get-to-the-FTP-pixel-through-the-online-SSL-interface!-120863",
#         "Try-to-transmit-the-HTTP-card-maybe-it-will-override-the-multi-byte-hard-drive!-120863",
#         "Try-to-generate-the-TCP-bus-maybe-it-will-override-the-neural-bandwidth!-120863",
#         "You-cant-transmit-the-firewall-without-copying-the-1080p-SDD-interface!-120863",
#         "You-cant-connect-the-interface-without-programming-the-virtual-PNG-protocol!-120863",
#         "Try-to-bypass-the-SAS-card-maybe-it-will-transmit-the-solid-state-system!-120863",
#         "Use-the-auxiliary-EXE-monitor-then-you-can-hack-the-haptic-port!-120863",
#     ]
#     time0 = time.perf_counter()
#     for slug in slug_list:
#         print(fetch_data(f'https://api.realworld.io/api/articles/{slug}').text)
#     time1 = time.perf_counter()
#     print(time1 - time0)

# main()