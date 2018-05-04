"""
多线程
threading模块
"""
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('11_1_output_formatting.py', 'myacchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()
print('Main program waited untile background was done.')

