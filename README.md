# Auto_Download_Torrents_From_PTSite
A easy way to download torrents from private tracker sites with poor coding.

Update log:
2019/06/29
1. Integrating the function of downloading in NexusPHP sites, NexusPHP but encrypted download url sites and GazellePHP sites in one script. (Only tested in MT(normal nexusphp), HDC(encrypted) & DIC(gzphp) , not compatible with PTP)
2. Added an function to record the torrents has downloaded by creating an .log file in monitor path.
3. Perfecting the method of completing Headers' information.

2019/06/04
1. Added some lines to ensure that the script could download torrents correctly.
2. Added a new script to handle the encrypted torrent's download url.
  
  
  
  
  
Usage shows below:  
用法如下，将根据注释进行解释：  
  
  
#### The requirements shows above, please use these commands to install the requirements in commandline. Using "sudo" in the case of meeting Permission problems.
#### 使用前请先在命令行中安装需要的包, 看情况选择要不要用sudo:
pip install bs4  
pip install requests  
pip install lxml  
  
  
#### Complete the variables below:
#### 完成下列的变量
#### Some examples: 
site_name = "M-TEAM"  
site_url = "https://tp.m-team.cc/torrents.php"  
site_cookie = "c_lang_folder=cht; tp=I2ODOGYNDFmZDdASDASODU3ZDA1ZU3ZDAYxNDFmZDdhYWRhZmRlOA%3D%3D"  
url_half = "https://tp.m-team.cc/"  
  
site_name = "xxxxx"  
site_url = "https://xxxxxxxxx/torrents.php"  
site_cookie = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
#### 如何获取cookie请自行学习
  
  

#### It always would be the first part of your site, like: url_half = "https://tp.m-team.cc/"
#### 一般来讲，这个变量就是你的网站的前半部分
url_half = "https://xxxxxxxxxxxxxxxxx/"


#### If your site is a Gazelle Site, please change this varible to True, like: is_gazelle = True
#### 如果是Gazelle构架，需要改成“is_gazelle = True”，经查发现，JPOP还有需要改其他变量才能使用，PTP无法使用，暂时确定能用的gz网站只有DIC
is_gazelle = False  
  
#### If the torrents' download url in your site were encrypted like HDC, please change this varible to True, like: is_encrypted = True
#### 如果网站的种子下载地址，鼠标指上去发现跟种子ID无关，或不仅仅是种子ID，还带有加密hash之类的，需要设置成 True, 暂时发现的加密站为HDC，改成True后可用
is_encrypted = False  
  
#### 下面这个' url_last = ""  '现在不需要了
#### Check the download url, especially when you are using a https(SSL) url.
#### Some torrents' download pages url could be "https://tp.m-team.cc/download.php?id=xxxxx&https=1", in this case, you need to assign the variable of "url_last". Examples:url_last = "&https=1"
url_last = ""  
  
  
#### If you couldn't downlaod the torrents to your directory where the *.py script is, you could just define the variables below. Make sure the format of your path because of the difference between Windows and Linux.
#### Example of windows:              monitor_path = r'C:\\Users\\DELL-01\\Desktop\\'       Don't forget the last '\\'
#### Example of Linux and MacOS:      monitor_path = r'/home/user/Downloads/'               Don't forget the last '/'
#### 设置一个目录，下载软件监控这个目录，目录里的种子自动添加。可以不设置，一般会下载到脚本所在目录，或用户家目录。
#### win下和linux下的路径表达方式不同，注意区分。
#### win下：   monitor_path = r'C:\\Users\\DELL-01\\Desktop\\'
#### linux下： monitor_path = r'/home/user/Downloads/'
monitor_path = r''  
