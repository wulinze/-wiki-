
class Urlmanager:
    url_set = set()

    def __init__(self, url):
        self.url_set = {url}

    def add_url(self, url):
        self.url_set.add(url)

    def del_url(self, url):
        if url in list(self.url_set):
            self.url_set.remove(url)

    def get_url(self):
        if self.get_len() > 0:
            return list(self.url_set)[0]

    def get_len(self):
        return len(self.url_set)
