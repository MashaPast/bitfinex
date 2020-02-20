import asyncio
import websockets
from logger import appLogger
import json
from helpers_ws.helpers_ws import LIST_OF_ARGVALUES
#import pytest

uri = "wss://api-pub.bitfinex.com/ws/2"

symbol = LIST_OF_ARGVALUES[58]


#@pytest.fixture(name = 'test_subscribe_to_action')
async def start_client():
    appLogger.debug('Start connection')
    ws_connection = await websockets.connect(uri)
    return ws_connection

#@pytest.mark.asyncio
async def subscribe_to_action(ws_connection):
    appLogger.debug('Subscribing to server')
    await ws_connection.send('{ "event": "subscribe", "channel": "ticker", "symbol": "t' + str(symbol) + '"}')

    async for message in ws_connection: #permanently
        server_message = json.loads(message)
        if isinstance(server_message, dict):
            print("Info message: {}".format(server_message))
        if isinstance(server_message, list):
            if server_message[1] == 'hb':
                print("Heartbeat server message: {}. There is no activity in the channel for 5 seconds".format(server_message))
            else:
                print("Stream response message: {}".format(server_message))
                check_type(server_message)
        with open('ws.txt', "w") as file:
            file.write(message)


def check_type(message_to_check):
    for i in range(0, len(message_to_check)):
        if isinstance(message_to_check[i], list):
            for j in range(1, len(message_to_check[i])):
                field_type = (type(message_to_check[i][j]))
                print(field_type) #float or int
        else:
            print(isinstance(message_to_check[i], int)) #must return True



ws = asyncio.get_event_loop().run_until_complete(start_client())
response = asyncio.get_event_loop().run_until_complete(subscribe_to_action(ws))

