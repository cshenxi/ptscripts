import bs4
import requests
import re
import os
import lxml

# READ me: 
# In some website, the torrents' download urls shows a encrypted url, so you cannot download the torrents by download urls directly, and you will find a 'hash' in the url without the torrent ID, like 'https://hdchina.org/download.php?hash=gUDK222e68f39LBWvYByug,,'.
# This is the reason why I build this script.

# Complete the variables below:
# Some examples: 
#site_name = "HDC"
#site_url = "https://hdchina.org/torrents.php"
#site_cookie = "__cfduid=d9asdb75e37f06e24134129asd010; PHPSESSID=1hWqjklEErYzaf6u-Jcu; hdchina=d8a2ee0762f1234123cb6eec1dd135f093adf315963c5e4059384"
################# IN THIS SCRIPT, 'URL_HALF' SHOULD BE THE TORRENT DETAIL PAGE's THE FIRST HALF URL ** NOT THE DOWNLOAD URL ##############
#url_half = "https://hdchina.org/details.php?id="

site_name = "xxxxx"
site_url = "https://xxxxxxxxx/torrents.php"
site_cookie = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url_half = "https://hdchina.org/details.php?id="


# Check the torrent's detail page's url.
# Some torrents' detail pages url could be "https://hdchina.org/details.php?id==xxxxx&hit=1", in this case, you need to assign the variable of "url_last". Examples:
# url_last = "&hit=1"
################### THE SAME WITH URL_HALF IN THIS SCRIPT #################
url_last = "&hit=1"


# If you couldn't downlaod the torrents to your directory where the *.py script is, you could just define the variables below. Make sure the format of your path because of the difference between Windows and Linux.
# Example of windows:              monitor_path = r'C:\\Users\\DELL-01\\Desktop\\'       Don't forget the last '\\'
# Example of Linux and MacOS:      monitor_path = r'/home/user/Downloads/'               Don't forget the last '/'
monitor_path = r''


# Other informations for safer sites. Complete it if you cannot download torrents.
# Some examples: 
#user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#referer = 'https://hdchina.org/index.php'
#host = 'hdchina.org'

user_agent = ''
referer = ''
host = ''

##^^^^^^^^^^^^^^^^^^^^^^^ YOU ONLY NEED TO ASSIGN VARIABLES SHOWS BEFORE ^^^^^^^^^^^^^^^^^^^^^^^^^^^##


# Using Session to keep cookie
cookie_dict = {"cookie":site_cookie}
s = requests.Session()
s.cookies.update(cookie_dict)
my_headers = {'User-Agent':user_agent, 'Referer':referer, 'Host':host}

pattern = r'id=(\d+)'

#####
def requests_check_headers(url):
    if user_agent or referer or host: 
        res = s.get(url, headers=my_headers)
    else:
        res = s.get(url)
    return res
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
        download_page = url_half + self.torrent[0] + url_last
        if self.torrent[1]:
            response = requests_check_headers(download_page)
            soup = bs4.BeautifulSoup(response.text,'lxml')
            down_url = soup.select_one('#clip_target')['href']
            res = requests_check_headers(down_url)
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
            print('\n\nPrinting the download statements: ')
            try:
                print('Downloading' + self.__str__())
            except:
                print('Cannot print the torrent name.')
            try:
                print('Writing torrent to your path ...')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
                with open(monitor_path + self.__str__(),'wb') as f:
                    f.write(res.content)
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
            except:
                print('Cannot write torrent file in your path!!')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
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
        res = requests_check_headers(site_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        self.raw_list = soup.select('.t_name')   ##### Careful!! It always should be ('.torrentname'). But in HDC it should be ('.t_name')
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print('\n\nThe website shows: ')
        try:
            print(soup)
        except:
            print('Cannot print soup')
        print('\n\nThe torrents informations(raw_list) shows below: ')
        try:
            print(self.raw_list)
        except:
            print('Cannot print raw_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
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
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print("\n\nThe torrents' free state tuples list shows below: ")
        try:
            print(free_state)
        except:
            print('Cannot print the free_tuple_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
        return free_state
#####
#####
task = Page()   ## The site would inform you that you have loged in this site when you run Page() at the very beginning.
task = Page()   ## So just run this command again to make sure that you can get the informations of torrents page.
task_list = task.Free()
#####
for torrent in task_list:
    torrent_name = str(Torrents(torrent))
    if os.path.isfile(monitor_path + torrent_name) == False:
        Torrents(torrent).DL()
    else:
        continue
#####