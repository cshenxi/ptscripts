import bs4
import requests
import re
import os

pattern = r'id=(\d+)'

site_name = "M-TEAM"
site_url = "https://tp.m-team.cc/torrents.php"
site_cookie = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url_half = "https://tp.m-team.cc/download.php?id="
user_agent = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
referer = 'https://tp.m-team.cc/login.php'
host = 'tp.m-team.cc'

# Check the download url, especially when you are using a https(SSL) url.
# Some torrents' download pages url could be "https://tp.m-team.cc/download.php?id=xxxxx&https=1", in this case, you need to assign the variable of "url_last = &https=1"
url_last = "&https=1"



# Using Session to keep cookie
cookie_dict = {"cookie":site_cookie}
s = requests.Session()
s.cookies.update(cookie_dict)
my_headers = {'User-Agent':user_agent, 'Referer':referer, 'Host':host}

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
        down_url = url_half + self.torrent[0] + url_last
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
        #res = s.get(site_url)                          # If you could login the site just by providing cookie, you can use this command and add a '#' before the below command.
        res = s.get(site_url, headers=my_headers)    # You may provide full informations of Headers if the site has a higher safe level.
        soup = bs4.BeautifulSoup(res.text,'lxml')
        self.raw_list = soup.select('.torrentname')

    def __str__(self):
        return self.raw_list
    
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
task = Page()   ## The site would inform you that you have loged in this site when you run Page() at the very beginning.
task = Page()   ## So just run this command again to make sure that you can get the informations of torrents page.
task_list = task.Free()
#####
for torrent in task_list:
    torrent_name = str(Torrents(torrent))
    if os.path.isfile(torrent_name) == False:
        Torrents(torrent).DL()
    else:
        continue
#####