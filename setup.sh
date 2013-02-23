#########################################################################
# File Name: setup.sh
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2013年02月23日 星期六 14时20分05秒
#########################################################################
#!/bin/bash
sudo apt-get install python-setuptools mpg123 -y
sudo easy_install web.py
wget https://github.com/ma6174/fmpi/archive/master.zip
unzip master.zip
cd fmpi-master
ifconfig | grep addr
echo "安装部署完成，请根据上面的IP在电脑浏览器上打开http://树莓派IP:8000/"
bash start.sh
