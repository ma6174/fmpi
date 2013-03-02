#########################################################################
# File Name: setup.sh
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2013年02月23日 星期六 14时20分05秒
#########################################################################
#!/bin/bash
sudo apt-get install python-setuptools mpg123 -y
sudo easy_install web.py
sudo easy_install wsgilog
wget https://github.com/ma6174/fmpi/archive/master.zip
unzip master.zip
cd fmpi-master
sudo cp pifm /usr/bin/
