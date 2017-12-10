# -*- coding: utf-8 -*-
from autobahn.asyncio.websocket import WebSocketServerProtocol


class ChttWebSocketProtocol(WebSocketServerProtocol):
    def __init__(self):
        super(ChttWebSocketProtocol, self).__init__()
        self.username = None
