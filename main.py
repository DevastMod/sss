import asyncio
import websockets

while True:
    async def Spam():
        async with websockets.connect("wss://devast69.devast.io:433") as websocket:
            await websocket.send("[30,"12345678901234567890","0",-1,0,"bit.ly/devastmod",0,null,0]")
            # await websocket.recv()

    asyncio.run(Spam())
