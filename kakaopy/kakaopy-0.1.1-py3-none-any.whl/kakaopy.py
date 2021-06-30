import requests
import urllib.request
import json

header = {}

def setHeader(restAPI) :
    header['Authorization'] = "KakaoAK "+ restAPI

class doc:

    def setData(self, sort, page, size):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)

    def setSort(self, sort):
        if sort == "accuracy" or sort == "recency":
            self.sort = sort
        else :
            print("sort is accuracy or recency")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)


    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v2/search/web"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10


class video:
    
    def setData(self, sort, page, size):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)
    
    def setSort(self, sort):
        if sort == "accuracy" or sort == "recency":
            self.sort = sort
        else :
            print("sort is accuracy or recency")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)

    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v2/search/vclip"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10

class image:
    
    def setData(self, sort, page, size):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)
    
    def setSort(self, sort):
        if sort == "accuracy" or sort == "recency":
            self.sort = sort
        else :
            print("sort is accuracy or recency")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)

    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v2/search/image"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10

class blog:
    
    def setData(self, sort, page, size):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)
    
    def setSort(self, sort):
        if sort == "accuracy" or sort == "recency":
            self.sort = sort
        else :
            print("sort is accuracy or recency")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)

    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v2/search/blog"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10

class book:
    
    def setData(self, sort, page, size, target):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)
        self.setTarget(self,target)
    
    def setSort(self, sort):
        if sort == "accuracy" or sort == "latest":
            self.sort = sort
        else :
            print("sort is accuracy or latest")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def setTarget(self, target):
        if target in ["title", "isbn", "publisher", "person"] :
            self.target = target
        else :
            print("title, isbn, publisher, person")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)
        if self.target != "":
            queryString += "&target="+self.target

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)

    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v3/search/book"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10
        self.target = ""

class cafe:
    
    def setData(self, sort, page, size):
        self.setSort(self, sort)
        self.setPage(self, page)
        self.setSize(self, size)
    
    def setSort(self, sort):
        if sort == "accuracy" or sort == "recency":
            self.sort = sort
        else :
            print("sort is accuracy or recency")

    def setPage(self, page):
        if 1 <= page and page <= 50:
            self.page = page
        else :
            print("1 <= page <= 50")

    def setSize(self, size):
        if 1<= size and size <= 50 :
            self.size = size
        else :
            print("1 <= size <= 50")

    def search(self, query:str):
        try :
            Text = urllib.parse.quote(query)
        except:
            print("query has problem")
            return
        
        queryString = "?query="+Text+"&sort="+self.sort+"&page="+str(self.page)+"&size="+str(self.size)

        r = requests.get(self.url + queryString, headers=header)
        return json.loads(r.text)

    def save(self, query:str, path:str):
        data = self.search(query)
        if ".json" not in path:
            path = path + ".json"
        with open(path, 'w', encoding = 'utf-8') as outfile:
            outfile.write(json.dumps(data, ensure_ascii = False))
            print("saved!")

    def __init__(self):
        self.query =""
        self.url = "https://dapi.kakao.com/v2/search/cafe"
        self.sort = "accuracy"
        self.page = 1
        self.size = 10