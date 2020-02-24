import asyncio
import websockets
from logger import appLogger
import json
from helpers_ws.helpers_ws import LIST_OF_ARGVALUES, URI
import pytest




symbol = LIST_OF_ARGVALUES[58]

@pytest.mark.asyncio
@pytest.fixture()
async def connection_fixture(event_loop):
    appLogger.debug('Start connection')
    ws_connection = await websockets.connect(URI)
    yield ws_connection
    await ws_connection.close()

@pytest.mark.asyncio
#@pytest.mark.parametrize(('symbol'), LIST_OF_ARGVALUES[0:20])
async def test_subscribe_to_action(connection_fixture):

    appLogger.debug('Subscribing to server')
    await connection_fixture.send('{ "event": "subscribe", "channel": "ticker", "symbol": "t' + str(symbol) + '"}')

    async for message in connection_fixture: #permanently
        server_message = json.loads(message)
        if isinstance(server_message, dict):
            if server_message['event'] == 'info':
                print("Info message 1: {}".format(server_message))
            if server_message['event'] == 'subscribed':
                assert server_message['event'] == 'subscribed'
                print("Info message 2: {}".format(server_message))
                break
            if server_message['event'] == 'error':
                print("Response-failure: {}".format(server_message))
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
            for j in range(0, len(message_to_check[i])):
                field_type = (type(message_to_check[i][j]))
                print(field_type) #float or int
        else:
            print(isinstance(message_to_check[i], int)) #must return True



#     # ws = asyncio.get_event_loop().run_until_complete(start_ws_client())
#     # response = asyncio.get_event_loop().run_until_complete(subscribe_to_action(ws))