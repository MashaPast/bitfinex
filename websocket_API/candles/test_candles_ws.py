import asyncio
import websockets
from logger import appLogger
import json
from helpers_ws.helpers_ws import LIST_OF_ARGVALUES, check_type
import pytest

channel = "trades"


@pytest.mark.asyncio
@pytest.mark.parametrize(('symbol'), LIST_OF_ARGVALUES[0:20])
async def test_subscribe_to_action(connection_fixture, symbol):

    appLogger.debug('Subscribing to server')
    await connection_fixture.send('{ "event": "subscribe", "channel": "' + str(channel) + '", "symbol": "t' + str(symbol) + '"}')

    async for message in connection_fixture: #permanently
        server_message = json.loads(message)
        if isinstance(server_message, dict):
            if server_message['event'] == 'info':
                print("Info message 1: {}".format(server_message))
            elif server_message['event'] == 'subscribed':
                print("Info message 2: {}".format(server_message))
            elif server_message['event'] == 'error':
                print("Response-failure: {}".format(server_message))
        elif isinstance(server_message, list):
            if server_message[1] == 'hb':
                print("Heartbeat server message: {}. There is no activity in the channel for 5 seconds".format(server_message))
            else:
                print("Stream response message: {}".format(server_message))
                types_list = check_type(server_message)
                print(types_list)
                list_of_types = check_type(server_message)
                for i in range(0, len(server_message)):
                    assert isinstance(server_message[0], int)
                for types in list_of_types:
                    assert isinstance(types, float) or isinstance(types, int)
                break
