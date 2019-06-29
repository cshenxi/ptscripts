import bs4
import requests
import os
import lxml
import re

# Complete the variables below:
# Some examples: 
#site_name = "M-TEAM"
#site_url = "https://tp.m-team.cc/torrents.php"
#site_cookie = "c_lang_folder=cht; tp=I2ODOGYNDFmZDdASDASODU3ZDA1ZU3ZDAYxNDFmZDdhYWRhZmRlOA%3D%3D"
#url_half = "https://tp.m-team.cc/"

site_name = "xxxxx"
site_url = "https://xxxxxxxxx/torrents.php"
site_cookie = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# It always would be the first part of your site, like: url_half = "https://tp.m-team.cc/"
url_half = "https://xxxxxxxxxxxxxxxxx/"


# If your site is a Gazelle Site, please change this varible to True, like: is_gazelle = True
is_gazelle = False

# If the torrents' download url in your site were encrypted like HDC, please change this varible to True, like: is_encrypted = True
is_encrypted = False

# Check the download url, especially when you are using a https(SSL) url.
# Some torrents' download pages url could be "https://tp.m-team.cc/download.php?id=xxxxx&https=1", in this case, you need to assign the variable of "url_last". Examples:
# url_last = "&https=1"
#url_last = ""


# If you couldn't downlaod the torrents to your directory where the *.py script is, you could just define the variables below. Make sure the format of your path because of the difference between Windows and Linux.
# Example of windows:              monitor_path = r'C:\\Users\\DELL-01\\Desktop\\'       Don't forget the last '\\'
# Example of Linux and MacOS:      monitor_path = r'/home/user/Downloads/'               Don't forget the last '/'
monitor_path = r''


# Other informations for safer sites. Complete it if you cannot download torrents.
# Some examples: 
#user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#referer = 'https://tp.m-team.cc/login.php'
#host = 'tp.m-team.cc'

user_agent = ''

# You don't need to define the variables shows below unless you couldn't download the torrents after defined the above one
referer = ''
host = ''

# You don't need to define the variables shows below unless you couldn't download the torrents after defined the above two
upgrade_insecure_requests = ''
dnt = ''
accept_language = ''
accept_encoding = ''
accept = ''
cache_control = ''
content_length = ''
content_type = ''
origin = ''
accept_encoding = ''


# Only if you just want to check the first 10 torrents is free in the page and download the free torrents in this small amount, please change it to 10
# like: torrents_amount = 10
# We always grab all the torrents in the whole page, but you can define the amount of grabing torrents by defining the variable below 
torrents_amount = 0

# You don't need to change this variables unless you cannot download from your GAZELLE site
# check this value from the page source code
colspan = '3'

# You don't need to change this variables unless you cannot find free torrents correctly
free_tag = 'pro_free'
free_tag2 = 'pro_free2up'
DIC_free_tag = 'torrent_label tooltip tl_free'
#PTP_free_tag = 'torrent-info__download-modifier--free'

torrents_class_name = '.torrentname'
HDC_torrents_class_name = '.t_name'
DIC_torrents_class_name = '.td_info'
#PTP_torrents_class_name = '.basic-movie-list__torrent-row--user-seeding'

download_class_name = '.rowfollow'
HDC_download_class_name = '.torrentdown_button'



##^^^^^^^^^^^^^^^^^^^^^^^ YOU ONLY NEED TO ASSIGN VARIABLES SHOWS BEFORE ^^^^^^^^^^^^^^^^^^^^^^^^^^^##



# Using Session to keep cookie
cookie_dict = {"cookie":site_cookie}
s = requests.Session()
s.cookies.update(cookie_dict)
pattern = r'id=(\d+)'


#####
def get_my_headers(my_headers = {}):
    '''
    Make a proper headers dictionary
    '''
    if user_agent:
        my_headers['User-Agent'] = user_agent
    if referer:
        my_headers['Referer'] = referer
    if host:
        my_headers['Host'] = host
    if accept:
        my_headers['accept'] = accept
    if accept_language:
        my_headers['accept-language'] = accept_language
    if accept_encoding:
        my_headers['accept-encoding'] = accept_encoding
    if origin:
        my_headers['origin'] = origin
    if dnt:
        my_headers['dnt'] = dnt
    if upgrade_insecure_requests:
        my_headers['upgrade-insecure-requests'] = upgrade_insecure_requests
    #if cookie:
    #    my_headers['cookie'] = cookie
    if cache_control:
        my_headers['cache-control'] = cache_control
    if content_length:
        my_headers['content-length'] = content_length
    if content_type:
        my_headers['content-type'] = content_type
    
    return my_headers
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
        return '{}_{}.torrent'.format(site_name,self.torrent[1])
    
    def download(self):
        '''
        A function to download a free torrent.
        '''
        down_url = url_half + self.torrent[3] #+ url_last
        if self.torrent[0]:
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

    def encrypted_download(self, download_class_name):
        '''
        A function to download a free torrent.
        '''
        download_page = url_half + self.torrent[2]
        if self.torrent[0]:
            response = requests_check_headers(download_page)
            soup = bs4.BeautifulSoup(response.text,'lxml')
            # down_url_last = soup.select_one(download_class_name).a['href']   # For other sites
            down_url_last = soup.select_one(download_class_name)['href']   # Just for HDC, common way, but different from other sites either
            down_url = url_half + down_url_last
            # down_url = soup.select_one('#clip_target')['href']    # a faster way For HDC only
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
class NexusPage():
    '''
    Getting a torrent page with all torrents in it
    '''
    def __init__(self, torrents_class_name):
        self.torrents_list = []
        self.processed_list = []
        self.torrents_class_name = torrents_class_name
        
        # Requesting page information of torrents by session
        res = requests_check_headers(site_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        self.processed_list = soup.select(self.torrents_class_name)
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print('\n\nThe website shows: ')
        try:
            print(str(soup))
        except:
            print('Cannot print soup')
        print('\n\nThe torrents informations(processed_list) shows below: ')
        try:
            print(self.processed_list)
        except:
            print('Cannot print processed_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
    def __str__(self):
        return self.processed_list
    
    def find_free(self, free_tag, free_tag2=''):
        free_state = []
        # Check free and add states
        for entry in self.processed_list:            
            details = entry.a['href']
            torrent_id = re.search(pattern, details).group(1)
            
            #if torrent is free:
            if entry.find(class_=free_tag) or entry.find(class_=free_tag2):
                last_download_url = 'NULL'
                # Find the tag that download url in
                for subentry in entry.select('.embedded'):
                    if 'href="download.php?' in str(subentry):
                        last_download_url = subentry.a['href']
                free_state.append((True, torrent_id, details, last_download_url))
            else:
                free_state.append((False, torrent_id, details, "NULL"))
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print("\n\nThe torrents' free state tuples list shows below: ")
        try:
            print(free_state)
        except:
            print('Cannot print the free_tuple_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
        return free_state
#####
class GazellePage():
    '''
    Getting a torrent page with all torrents in it
    '''
    def __init__(self, torrents_class_name):
        self.torrents_list = []
        self.processed_list = []
        self.torrents_class_name = torrents_class_name
        
        # Requesting page information of torrents by session
        res = requests_check_headers(site_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        self.torrents_list = soup.select(self.torrents_class_name)

        # Choosing the first line or the last third line based on the site source code
        #self.processed_list = self.torrents_list
        for entry in self.torrents_list:
            if entry['colspan'] == colspan:
                self.processed_list.append(entry)
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print('\n\nThe website shows: ')
        try:
            print(str(soup))
        except:
            print('Cannot print soup')
        print('\n\nThe torrents informations(processed_list) shows below: ')
        try:
            print(self.processed_list)
        except:
            print('Cannot print processed_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
    def __str__(self):
        return self.processed_list
    
    def find_free(self, free_tag, free_tag2=''):
        free_state = []
        # Check free and add states
        for entry in self.processed_list:
            last_download_url = entry.a['href']
            torrent_id = re.search(pattern, last_download_url).group(1)
            details = 'torrents.php?id=' + torrent_id
            
            #if torrent is free:
            if entry.find(class_=free_tag) or entry.find(class_=free_tag2):
                free_state.append((True, torrent_id, details, last_download_url))
            else:
                free_state.append((False, torrent_id, details, last_download_url))
#vvvvvvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvv# Command for debug #vvvvvvvvvvvvvvvvvvvvvv#
        print("\n\nThe torrents' free state tuples list shows below: ")
        try:
            print(free_state)
        except:
            print('Cannot print the free_tuple_list')
#^^^^^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^# Command for debug #^^^^^^^^^^^^^^^^^^^^^^#
        return free_state
#####
def download_free(torrents_amount, task_list, monitor_path):
    if os.path.isfile(monitor_path + "downloaded_list.log") == False:
        with open(monitor_path + "downloaded_list.log", 'w') as f:
            f.write("A list shows the torrents have been downloaded:\n")

    if not torrents_amount:
        for torrent in task_list:
            torrent_name = str(Torrents(torrent))
            with open(monitor_path + "downloaded_list.log", 'r') as f:
                downloaded = f.read()
                if torrent_name in downloaded:
                    continue
            with open(monitor_path + "downloaded_list.log", 'a') as f:
                f.write(torrent_name)

            if os.path.isfile(monitor_path + torrent_name) == False:
                Torrents(torrent).download()
            else:
                continue
    else:
        for torrent in task_list[0:torrents_amount:1]:
            torrent_name = str(Torrents(torrent))

            with open(monitor_path + "downloaded_list.log", 'r') as f:
                downloaded = f.read()
                if torrent_name in downloaded:
                    continue
            with open(monitor_path + "downloaded_list.log", 'a') as f:
                f.write(torrent_name)

            if os.path.isfile(monitor_path + torrent_name) == False:
                Torrents(torrent).download()
            else:
                continue
#####
def download_encrypted_free(torrents_amount, task_list, monitor_path, download_class_name):
    if os.path.isfile(monitor_path + "downloaded_list.log") == False:
        with open(monitor_path + "downloaded_list.log", 'w') as f:
            f.write("A list shows the torrents have been downloaded:\n")
            
    if not torrents_amount:
        for torrent in task_list:
            torrent_name = str(Torrents(torrent))

            with open(monitor_path + "downloaded_list.log", 'r') as f:
                downloaded = f.read()
                if torrent_name in downloaded:
                    continue
            with open(monitor_path + "downloaded_list.log", 'a') as f:
                f.write(torrent_name)

            if os.path.isfile(monitor_path + torrent_name) == False:
                Torrents(torrent).encrypted_download(download_class_name)
            else:
                continue
    else:
        for torrent in task_list[0:torrents_amount:1]:
            torrent_name = str(Torrents(torrent))

            with open(monitor_path + "downloaded_list.log", 'r') as f:
                downloaded = f.read()
                if torrent_name in downloaded:
                    continue
            with open(monitor_path + "downloaded_list.log", 'a') as f:
                f.write(torrent_name)

            if os.path.isfile(monitor_path + torrent_name) == False:
                Torrents(torrent).encrypted_download(download_class_name)
            else:
                continue
#####
#####
#####
my_headers = get_my_headers(my_headers = {})

if not is_gazelle:
    if not is_encrypted:
        task = NexusPage(torrents_class_name)   ## The site would inform you that you have loged in this site when you run Page() at the very beginning.
        task = NexusPage(torrents_class_name)   ## So just run this command again to make sure that you can get the informations of torrents page.
        task_list = task.find_free(free_tag,free_tag2)
        download_free(torrents_amount, task_list, monitor_path)
    else:
        task = NexusPage(HDC_torrents_class_name)   ## The site would inform you that you have loged in this site when you run Page() at the very beginning.
        task = NexusPage(HDC_torrents_class_name)   ## So just run this command again to make sure that you can get the informations of torrents page.
        task_list = task.find_free(free_tag,free_tag2)
        download_encrypted_free(torrents_amount, task_list, monitor_path, HDC_download_class_name)
#####
else:
    task = GazellePage(DIC_torrents_class_name)   ## The site would inform you that you have loged in this site when you run Page() at the very beginning.
    task = GazellePage(DIC_torrents_class_name)   ## So just run this command again to make sure that you can get the informations of torrents page.
    task_list = task.find_free(DIC_free_tag)
    download_free(torrents_amount, task_list, monitor_path)