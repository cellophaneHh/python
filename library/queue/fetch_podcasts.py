from queue import Queue
import threading
import urllib
from urllib.parse import urlparse
import typing

import feedparser

num_fetch_threads = 2
enclosure_queue = Queue()

feed_urls = ['http://talkpython.fm/episodes/rss']


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(q):
    '''
    this is the worker thread function.
    it processes items in the queue one after another.
    These daemon threads go into an infinite loop, and
    exit only when the main thread ends
    '''
    while True:
        message('looking for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        print(type(q))
        q.task_done()


for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue, ),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()

for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
