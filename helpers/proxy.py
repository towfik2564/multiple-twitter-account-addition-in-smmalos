from .scraper import Scraper

class Proxy():

    def __init__(self):
        self.scraper = Scraper('https://free-proxy-list.net/', True)
    
    def proxie_list(self):
        th_collection = self.scraper.find_elements('div.fpl-list table thead th')
        del th_collection[len(th_collection)-1]
        for th in th_collection:
            th = th.lower()
            th = th.replace(' ', '_')
        td_collection = self.scraper.find_elements('div.fpl-list table tbody tr')
        proxies = []
        for td in td_collection:
            td = td.split(' ')
            val = td[0] + ':' + td[1]
            proxies.append(val)
        return proxies
