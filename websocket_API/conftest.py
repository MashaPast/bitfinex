import pytest
from logger import appLogger
import websockets
from helpers_ws.helpers_ws import URI


@pytest.mark.asyncio
@pytest.fixture()
async def connection_fixture(event_loop):
    appLogger.debug('Start connection')
    ws_connection = await websockets.connect(URI)
    yield ws_connection
    await ws_connection.close()