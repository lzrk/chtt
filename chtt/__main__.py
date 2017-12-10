# -*- coding: utf-8 -*-
import asyncio
from autobahn.asyncio.websocket import WebSocketServerFactory
from .protocol import ChttWebSocketProtocol


if __name__ == '__main__':
    factory = WebSocketServerFactory()
    factory.protocol = ChttWebSocketProtocol

    loop = asyncio.get_event_loop()

    server = loop.run_until_complete(
        loop.create_server(factory, '0.0.0.0', '7777')
    )
    loop.run_forever()
