#!/usr/bin/python
# -*- coding: gbk -*-
import os 
import time 
import sys 
#备份的源文件路径 
source = ['D:/ED汉化/brzjomo.xml'] 
#备份的文件所放的地方 
target_dir = 'E:/备份/' 
#备份文件的名字 
target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
#zip_command="7z a %s %s" %(target,' '.join(source))  
zip_command="7z a %s %s" %(target,' '.join(source)) 
if os.system(zip_command) == 0: 
  print ('成功打包至' + " " + "---" + target + "---")
else: 
  print ('打包失败！')
  print ('请检查路径和环境变量是否正确！')
time.sleep(3)
