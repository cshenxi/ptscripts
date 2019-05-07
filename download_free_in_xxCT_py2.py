import bs4
import requests
import re
import os

site_name = "xxCT"
site_url = "https://xxxxxx.org/torrents.php"
site_cookie = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url_half = "https://xxxxxxxxxxxxxxxxxxxx.org/download.php?id="
pattern = r'id=(\d+)'

# Using Session to keep cookie
cookie_dict = {"cookie":site_cookie}
s = requests.Session()
s.cookies.update(cookie_dict)

#####
class Torrents():
    '''
    Define a torrent
    '''
    def __init__(self,torrent):
        self.torrent = torrent
        
    def __str__(self):
        return '{}_{}.torrent'.format(site_name,self.torrent[0])
    
    def DL(self):
        '''
        A function to download a free torrent.
        '''
        down_url = url_half + self.torrent[0]
        if self.torrent[1]:
            res = s.get(down_url)
            with open(self.__str__(),'wb') as f:
            	f.write(res.content)
        else:
            pass
#####
class Page():
    '''
    Getting a torrent page with all torrents in it
    '''
    def __init__(self):
        self.torrent_list = []
        self.raw_list = []
        
        # Requesting page information of torrents by session
        res = s.get(site_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        self.raw_list = soup.select('.torrentname')

    def __str__(self):
        amount = len(self.string_list)
        return "This page has {} torrents.".format(amount)
    
    def Free(self):
        free_state = []
        # Check free and add states
        for entry in self.raw_list:
            #if entry.find(class_='pro_free' 'pro_free2up'):
            if entry.find(class_='pro_free') or entry.find(class_='pro_free2up'):
                details = entry.a['href']
                torrent_id = re.search(pattern, details).group(1)
                free_state.append((torrent_id,True))
            else:
                details = entry.a['href']
                torrent_id = re.search(pattern, details).group(1)
                free_state.append((torrent_id,False))                
        return free_state
#####
task = Page()
task_list = task.Free()
#####
for torrent in task_list:
    torrent_name = str(Torrents(torrent))
    if os.path.isfile(torrent_name) == False:
        Torrents(torrent).DL()
    else:
        continue
#####