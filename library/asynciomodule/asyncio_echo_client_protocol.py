import asyncio
import functools
import logging
import sys

MESSAGES = [
    b'this is the message. ',
    b'it will be sent',
    b'in parts.',
]
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)


class EchoClient(asyncio.Protocol):
    def __init__(self, messages, future):
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log.debug('connection to {} port {}'.format(*self.address))
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('sending {!r}'.format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))

    def eof_received(self):
        self.log.debug('received EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed connection')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection_lost(exc)


SERVER_ADDRESS = ('localhost', 10000)
log = logging.getLogger('main')
loop = asyncio.get_event_loop()
client_completed = asyncio.Future()
client_factory = functools.partial(EchoClient,
                                   messages=MESSAGES,
                                   future=client_completed)

factory_coroutie = loop.create_connection(client_factory, *SERVER_ADDRESS)
log.debug('waiting for client to complete')
try:
    loop.run_until_complete(factory_coroutie)
    loop.run_until_complete(client_completed)
finally:
    log.debug('closing event loop')
    loop.close()
