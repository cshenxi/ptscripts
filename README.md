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
