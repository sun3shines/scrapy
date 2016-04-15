
from fastscrapy.parse.http import sendproxys
class Proxy:
    def __init__(self,attrs):
        self.attrs = attrs

    def save(self):
        sendproxys(self.attrs)
