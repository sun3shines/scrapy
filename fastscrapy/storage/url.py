
from fastscrapy.parse.http import sendurls
class Url:
    def __init__(self,urls,uuid):
        self.urls = urls
        self.uuid = uuid

    def save(self):
        sendurls(self.urls,self.uuid)


