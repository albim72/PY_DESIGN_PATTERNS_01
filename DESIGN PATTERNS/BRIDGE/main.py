import abc
import urllib.parse
import urllib.request

class ResourceContent:
    def __init__(self,imp):
        self._imp = imp
        
    def show_content(self,path):
        self._imp.fetch(path)
        
class ResourceContentFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self,path):
        pass
    
    
class URLFetcher(ResourceContentFetcher):
    def fetch(self,path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                this_page = response.read()
                print(this_page)
                
class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path) as f:
            print(f.read())
            
