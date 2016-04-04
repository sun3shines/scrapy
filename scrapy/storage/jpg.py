
import urllib
import os
import os.path

class Jpg:

    def __init__(self,src):
        self.src = src
        self.path = self.src.replace('http://','').replace('https://','')
        self.root = '/jpg'
        self.dir = self.root+ '/' + '/'.join(self.path.split('/')[:-1])
        self.last = self.path.split('/')[-1]
        self.full = self.dir + '/' + self.last

    def load(self):
        if not os.path.exists(self.dir):
            os.system('mkdir -p '+self.dir)

    def save(self):
        self.load()
        conn = urllib.urlopen(self.src)  
        with open(self.full,'wb') as f:
            f.write(conn.read())  

if __name__ == '__main__':
    src = 'http://pic.581r.com/d2/2258/225831-1.jpg'
    j = Jpg(src) 
    j.save()
    print j.dir + '/' + j.last
