import os
import time
import asyncio

# async def get_data():
#     out = await os.system("curl --request POST --url https://carnet.ai/recognize-file --header 'Connection: keep-alive' --header 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybL0pJQRNggqxuxMT' --header 'Postman-Token: 0cb3138e-d99c-4f25-ac42-30339903eff7' --header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' --header 'X-Requested-With: XMLHttpRequest' --header 'cache-control: no-cache' --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' --form imageFile=@/home/alinp25/HackTM/img.jpg")
#     return out

# # @asyncio.coroutine
# # async def coroutine_f():
# #     print('Da')
# #     out = get_data()
# #     # time.sleep(2)
# #     print(out)

# # while True:
# #     coroutine_f()
    
# loop = asyncio.get_event_loop()  
# loop.run_until_complete(get_data())  
# loop.close()  


# @asyncio.coroutine
# def slow_operation(future):
#     yield from os.system("curl --request POST --url https://carnet.ai/recognize-file --header 'Connection: keep-alive' --header 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybL0pJQRNggqxuxMT' --header 'Postman-Token: 0cb3138e-d99c-4f25-ac42-30339903eff7' --header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' --header 'X-Requested-With: XMLHttpRequest' --header 'cache-control: no-cache' --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' --form imageFile=@/home/alinp25/HackTM/img.jpg")
#     future.set_result('Future is done!')


# def got_result(future):
#     print(future.result())
#     loop.stop()

# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# future.add_done_callback(got_result)
# try:
#     loop.run_forever()
# finally:
#     loop.close()

while True:
    out = os.popen("curl --request POST --url https://carnet.ai/recognize-file --header 'Connection: keep-alive' --header 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybL0pJQRNggqxuxMT' --header 'Postman-Token: 0cb3138e-d99c-4f25-ac42-30339903eff7' --header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' --header 'X-Requested-With: XMLHttpRequest' --header 'cache-control: no-cache' --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' --form imageFile=@/home/alinp25/HackTM/img.jpg").read()
    time.sleep(2)
    print(out)
