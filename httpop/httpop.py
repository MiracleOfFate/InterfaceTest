import requests


class httpop:
    def api_get(self, url):
        res = requests.get(url)
        return res
