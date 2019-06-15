import asyncio
import logging
import sys


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger('EchoServer_{}_{}'.format(*self.address))
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('sent {!r}'.format(data))

    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        if error:
            self.log.error('ERROR: {}'.format(error))
        else:
            self.log.debug('closing')
        super().connection_lost(error)


SERVER_ADDRESS = ('localhost', 10000)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

loop = asyncio.get_event_loop()
factory = loop.create_server(EchoServer, *SERVER_ADDRESS)
server = loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))
try:
    loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    loop.close()
